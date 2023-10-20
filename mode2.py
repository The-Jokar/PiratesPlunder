from island import Island
from mode1 import Mode1Navigator
from data_structures.heap import MaxHeap

class Mode2Navigator:
    """
    In this mode 2 navigator it attempts to find the best move for each pirate to make, whether it is to plunder and island or do nothing, and then work out whihc island yields the best score should they chose to
    plunder. The implementation uses a number of lists as well as a dictionary, and a max heap to store and sort various information.
    """

    def __init__(self, n_pirates: int) -> None:
        """
        Inititialises the number of pirates that are in the battle,  a blank list that will contain islands a dictionary that will contain the island name and its score and a list containing island names
        :complexity: best and worst case is O(1)
        """
        self.n_pirates = n_pirates
<<<<<<< HEAD
        self.islands = []
        self.islands_dict = {}
        self.island_names = []
=======
        self.pirates_priority = MaxHeap(1)
>>>>>>> 6c01f9e3f670e823c1cf7a54f5dd27cc3f7b5b8d

    def add_islands(self, islands: list[Island]):
        """
        Adds a given list of islands to the navigator using a for loop and append
        :complexity: best and worst case complexity is O(n) where n is the length of the input list
        """
<<<<<<< HEAD
        #iterates through the islands and add them to a list as well adding their names to a seperate list
        for island in islands:
            self.islands.append(island)
            self.island_names.append(island.name)
            
=======
        if len(self.pirates_priority) == 0:
            self.pirates_priority = MaxHeap.heapify(islands)
        else:
            for island in islands:
                ratio = island.money / island.marines
                self.pirates_priority.add(island)
        print(len(self.pirates_priority))
>>>>>>> 6c01f9e3f670e823c1cf7a54f5dd27cc3f7b5b8d

    def simulate_day(self, crew: int) -> list[tuple[Island|None, int]]:
        """
        Approach: in this function I aimed to create a MaxHeap which would sort the islands by their respective scores, so it could then be use to determine what the best move for each pirate would be.
        the first step in this was to calculate the score from each island and then store it in a dictionary, with the key being the island name and the values being the scores. Next I would create a max heap,
        which contained all the scores inorder to sort them in order. The using a for loop I could iterate once through the sequence for each pirate, in the sequence we aim to check if they should plunder first, 
        then which island should be plundered and how many crew to send, and then finally updating the island.

        Purpose: this function return a list of tuples containing the choice for each pirates Island to attack, possibole None and how many crew they are sneding to attack,
        it determines this using a score calculated through a formula and then finds which option would yield the greatest score for each pirate

        :complexity: The best and worst case complexity of this function is (i + p*log(i)) where i is the number of islands, and p is the number of pirates, it occurs in all cases, as when considering an arbitrarily
        input there is no way to exit the function early
        """
<<<<<<< HEAD
        for island in self.islands:
            if island.marines > 0:
                max_money = min((crew/island.marines) * island.money, island.money)
                if max_money == island.money:
                    remaining_crew = crew - island.marines
                else:
                    remaining_crew = 0
            else:
                remaining_crew = crew
                max_money = 0
                
            island_score = 2 * (remaining_crew) + max_money
            self.islands_dict[island.name] = island_score
        
        heaped_scores= MaxHeap.heapify(list(self.islands_dict.values()))
        
        res = []
        for _ in range(self.n_pirates):
            max_score = heaped_scores.get_max()
            if max_score > 2 * crew:
                max_index = list(self.islands_dict.values()).index(max_score)
                island_index = self.island_names.index(list(self.islands_dict.keys())[max_index])
                island_choice = self.islands[island_index]
                max_money = min((crew/island_choice.marines) * island_choice.money, island_choice.money)
                if max_money == island_choice.money:
                    n_crew_sent = island_choice.marines
                else:
                    n_crew_sent = crew
                res.append((island_choice, n_crew_sent))
                island_update = self.update_island(island_choice, island_choice.money - max_money, island_choice.marines - n_crew_sent, crew)
                print("before", self.islands_dict)
                self.islands_dict.__delitem__(island_choice.name)
                print(island_update)
                self.islands_dict[island_update[1].name] = island_update[0]
                self.islands[island_index] = island_update[1]
                print("after", self.islands_dict)
                heaped_scores.add(island_update[0])
            else:
                res.append((None, 0))

        return res
    
    def update_island(self, island: Island, new_money, new_marines, crew) -> (float, Island):
            """
            This function acts as a helper function to simulate day, and updates an island that has been plundered returning
            its new score and the updated island
            :complexity: best and worst case is O(1)
            """
            new_island = Island(island.name, new_money, new_marines)
            if new_island.marines == 0:
                max_money = 0
                remaining_crew = crew
            else:
                max_money = min((crew/new_island.marines) * new_island.money, new_island.money)
                if max_money == new_island.money:
                    remaining_crew = crew - new_island.marines
                else:
                    remaining_crew = 0
                
            new_score = 2 * (remaining_crew) + max_money
            return (new_score, new_island)

=======
        raise NotImplementedError()

m2 = Mode2Navigator(4)
m2.add_islands([Island('a', 50, 3), Island('b', 70, 5), Island('c', 30, 1)])
>>>>>>> 6c01f9e3f670e823c1cf7a54f5dd27cc3f7b5b8d
