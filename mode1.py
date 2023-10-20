from island import Island
from data_structures.node import TreeNode
from data_structures.bst import BinarySearchTree

class Mode1Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117
    """

    def __init__(self, islands: list[Island], crew: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.crew = crew
        self.island_lst = islands
        self.islands = BinarySearchTree()
        for island in islands:
            marines = island.marines
            money = island.money
            ratio = marines / money
            self.islands.__setitem__(ratio, island)


    def select_islands(self) -> list[tuple[Island, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        iter_islands = self.islands.__iter__()
        res = []
        count = len(self.islands)
        old_crew = self.crew
        while self.crew >= 1 or count >= 1:
            try:
                cur_island = iter_islands.__next__()
            except:
                self.crew = old_crew   
                return res
            crew_ratio = self.crew / cur_island.item.marines
            if crew_ratio < 1:
                res.append((cur_island.item, self.crew))
                self.crew = old_crew   
                return res
            else:
                crew = cur_island.item.marines
                res.append((cur_island.item, crew))
                self.crew -= crew
            
            count -= 1
        self.crew = old_crew    
        return res

    def select_islands_from_crew_numbers(self, crew_numbers: list[int]) -> list[float]:
        """
        Student-TODO: Best/Worst Case
        """
        res = []
        for crew in crew_numbers:
            cur_crew = Mode1Navigator(self.island_lst, crew)
            islands = cur_crew.select_islands()
            max_money = 0
            for island in islands:
                max_money += (island[0].money * (island[1]/island[0].marines))
            res.append(max_money)
        
        return res
            

    def update_island(self, island: Island, new_money: float, new_marines: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        ratio = island.marines / island.money
        island = self.islands.__getitem__(ratio)
        self.islands.__delitem__(ratio)
        island.marines = new_marines
        island.money = new_money
        self.islands.__setitem__(ratio, island)