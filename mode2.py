from island import Island
from mode1 import Mode1Navigator
from data_structures.heap import MaxHeap

class Mode2Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117
    """

    def __init__(self, n_pirates: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.n_pirates = n_pirates
        self.pirates_priority = MaxHeap(1)

    def add_islands(self, islands: list[Island]):
        """
        Student-TODO: Best/Worst Case
        """
        if len(self.pirates_priority) == 0:
            self.pirates_priority = MaxHeap.heapify(islands)
        else:
            for island in islands:
                ratio = island.money / island.marines
                self.pirates_priority.add(island)
        print(len(self.pirates_priority))

    def simulate_day(self, crew: int) -> list[tuple[Island|None, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        raise NotImplementedError()

m2 = Mode2Navigator(4)
m2.add_islands([Island('a', 50, 3), Island('b', 70, 5), Island('c', 30, 1)])