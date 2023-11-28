from typing import Dict


class BusStop:
    def __init__(self, name: str):
        self.__name = name
        self.__line_num = []
        self.neighbours: Dict[BusStop, int] = {}

    def add_neighbour(self, new_name: str, weight: int) -> None:
        self.neighbours.update({BusStop(new_name): weight})

    @property
    def name(self):
        return self.__name

    @property
    def line_num(self):
        return self.__line_num

    def get_neighbours(self):
        return self.neighbours

    def add_line_num(self, line_num: str):
        if line_num not in self.__line_num:
            self.__line_num.append(line_num)

    def get_weight(self, neighbour: "BusStop"):
        return self.neighbours.get(neighbour, None)

    def __str__(self):
        return self.name

