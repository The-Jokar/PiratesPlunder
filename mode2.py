from island import Island
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
        self.islands = []
        self.islands_dict = {}
        self.island_names = []

    def add_islands(self, islands: list[Island]):
        """
        Adds a given list of islands to the navigator using a for loop and append
        :complexity: best and worst case complexity is O(n) where n is the length of the input list
        """
        #iterates through the islands and add them to a list as well adding their names to a seperate list
        for island in islands:
            self.islands.append(island)
            self.island_names.append(island.name)
            

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
        #first we iterate through the islands
        for island in self.islands:
            #checking if the island has marines
            if island.marines > 0:
                #first we calculate the max money that can be earned using the formula
                max_money = min((crew/island.marines) * island.money, island.money)
                #if the max money is the same as the sialnds then we are sending over an equal number of crew to marines
                if max_money == island.money:
                    #thus we reduce crew by the number of marines
                    remaining_crew = crew - island.marines
                else:
                    #if we made less money than the total that meant we sent all of our crew and has non remaining
                    remaining_crew = 0
            else:
                #if there are no marines then there is no money and we dont loose any crew
                remaining_crew = crew
                max_money = 0
            
            #calculate island score and then set values in the dictionary
            island_score = 2 * (remaining_crew) + max_money
            self.islands_dict[island.name] = island_score
        
        #create the heap using the scores
        heaped_scores= MaxHeap.heapify(list(self.islands_dict.values()))
        
        #create a results list
        res = []
        #iterate through the number of pirates
        for _ in range(self.n_pirates):
            #get the best score
            max_score = heaped_scores.get_max()
            #check if the max score from plundering the island is better than doing nothing
            if max_score > 2 * crew:
                #get the island using indexing and list
                max_index = list(self.islands_dict.values()).index(max_score)
                island_index = self.island_names.index(list(self.islands_dict.keys())[max_index])
                island_choice = self.islands[island_index]
                #calculate the max money
                max_money = min((crew/island_choice.marines) * island_choice.money, island_choice.money)
                #calculate the number of crew sent based on the amount of money earned
                if max_money == island_choice.money:
                    n_crew_sent = island_choice.marines
                else:
                    n_crew_sent = crew
                #append the choice
                res.append((island_choice, n_crew_sent))
                #update the island with the new money and marines after plundering caliing the update island function
                island_update = self.update_island(island_choice, island_choice.money - max_money, island_choice.marines - n_crew_sent, crew)
                #delete the old island
                self.islands_dict.__delitem__(island_choice.name)
                #add the new ilsand back into both the dictionary and the list
                self.islands_dict[island_update[1].name] = island_update[0]
                self.islands[island_index] = island_update[1]
                #readd the island with the updated values to the heap
                heaped_scores.add(island_update[0])
            else:
                #if it is not advatageous to plunder then do nothing
                res.append((None, 0))

        return res
    
    def update_island(self, island: Island, new_money, new_marines, crew) -> (float, Island):
            """
            This function acts as a helper function to simulate day, and updates an island that has been plundered returning
            its new score and the updated island
            :complexity: best and worst case is O(1)
            """
            #creates the new island with the updated values
            new_island = Island(island.name, new_money, new_marines)
            #check if new marines are zero if they are there is no money and crew remaining will be the crew
            if new_island.marines == 0:
                max_money = 0
                remaining_crew = crew
            else:
                #if there are still marines then calculate the max money adn remaining crew
                max_money = min((crew/new_island.marines) * new_island.money, new_island.money)
                if max_money == new_island.money:
                    remaining_crew = crew - new_island.marines
                else:
                    remaining_crew = 0
            #calculate the new score
            new_score = 2 * (remaining_crew) + max_money
            #return a tuple containg the score and the new island
            return (new_score, new_island)

