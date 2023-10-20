from island import Island
from data_structures.node import TreeNode
from data_structures.bst import BinarySearchTree

class Mode1Navigator:
    """
    In this class mode1 navigator given a number of islands and a crew size the pirate attempts to select the best island to plunder regardless of how many crew are lost. The class uses mainly a BST as well,
    as a list. By using a binary search tree in this task is allows us to use inorder traversal to easily traverse the ratio as the smallest ratio will be in the bottom left, and the smallest ratio will
    result in the largest amount of money able to be plundered. A bst also has good time complexity and considering the tree will be balanced is gives us O(logn) averge case complexity for most operations.
    """

    def __init__(self, islands: list[Island], crew: int) -> None:
        """
        Intitialises the crew size, islands, and BSt which sorts islands by their ratio of marines to money
        :complexity: best and worst case O(nlogn) where n is the number of islands in the list
        """
        #initialise variables
        self.crew = crew
        self.island_lst = islands
        #create a binarary search tree
        self.islands = BinarySearchTree()
        #add all the idlands to the tree using there marine to money ratio
        for island in islands:
            marines = island.marines
            money = island.money
            ratio = marines / money
            self.islands.__setitem__(ratio, island)


    def select_islands(self) -> list[tuple[Island, int]]:
        """
        Approach: when considering this function its important to take into account time compelxity by using while loop and an iterator we can achieve a worst case of O(n) and best case of O(logn)
        the while loop keeps attempting to move to the next item until there are no islands left or crew members left thsu ensuring that the maximum islands are visited, for each island we calculate the 
        maximum amount of money we can make and given our crew and the number fo marines. In order to maximise money it is important to send an equal amount of crew memebers as marines to each island where possible

        Purpose: this function resturns a list of tuples conating an ilsnad and how many crew mates are being sent to each islands, using the bst it using in order traversal to start at the sialnd with the best
        gold return until there are no crew or no islands

        :complexity: best case complexity is O(logn) where n is the number of islands in the bst, and the tree is balancedand the number of crew is less than the total number of marines, and worst case complexity is O(n) 
        where the total number of marines is greater that the number of crew
        """ 
        #create and iterator, result list, count and duplicate the original crew size
        iter_islands = self.islands.__iter__()
        res = []
        count = len(self.islands)
        old_crew = self.crew
        #using a while loop iterate until there are no more islands or no more crew
        while self.crew >= 1 or count >= 1:
            #try and retirve the next island
            try:
                cur_island = iter_islands.__next__()
            except:
                #if there are none left reset the crew and resturn the result
                self.crew = old_crew   
                return res
            #get the ratio of crew to marines
            crew_ratio = self.crew / cur_island.item.marines
            #if its less then only some money can be plundered
            if crew_ratio < 1:
                # so we send all crew to plunder as much as possible
                res.append((cur_island.item, self.crew))
                self.crew = old_crew   
                #then return the result
                return res
            else:
                #if we can plunder all the money then send all crew
                crew = cur_island.item.marines
                res.append((cur_island.item, crew))
                #update crew
                self.crew -= crew
            #reduce the island count by 1
            count -= 1
        #reset the crew size and return result
        self.crew = old_crew    
        return res

    def select_islands_from_crew_numbers(self, crew_numbers: list[int]) -> list[float]:
        """
        Approach: in this function we use a for loop to iterate through all the crew memebers followed by creating a new instance of this navigator with a different crew size allowing us to find all the possible islands
        that should be travelled to and from the calculate the maximum money that could be earned

        Purpose: this function returns the masimum amount of money a given crew size could earn

        :complexity: best and worst case is O(n * m) where n is the number fo islands and m is the len of the crew numers
        """
        res = []
        #iterate through the different crew numbers
        for crew in crew_numbers:
            #create an instance of mode1
            cur_crew = Mode1Navigator(self.island_lst, crew)
            #find all the possible islands that can bw gone to as well as the number of crew to send
            islands = cur_crew.select_islands()
            max_money = 0
            #calculate the max money given these islands and crew sent
            for island in islands:
                max_money += (island[0].money * (island[1]/island[0].marines))
            res.append(max_money)
        
        return res
            

    def update_island(self, island: Island, new_money: float, new_marines: int) -> None:
        """
        This function updates an island with its new values after is has been plunered 
        :complexity: best and worst case O(logn) where n is the number of islands in the tree
        """
        #get the islands ratio
        ratio = island.marines / island.money
        #get the islands
        island = self.islands.__getitem__(ratio)
        #delete the old ratio
        self.islands.__delitem__(ratio)
        #update the new money and marines and the set trhe new ratio and island in the bst
        island.marines = new_marines
        island.money = new_money
        self.islands.__setitem__(ratio, island)