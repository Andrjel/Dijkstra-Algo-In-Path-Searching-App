from typing import Dict


class BusStop:
    def __init__(self, name):
        self.__name = name
        self.neighbours: Dict[BusStop, int] = {}

    def add_neighbour(self, new_name: str, weight: int) -> None:
        self.neighbours.update({BusStop(new_name): weight})

    @property
    def name(self):
        return self.__name

    def get_neighbours(self):
        return self.neighbours.keys()

    def get_weight(self, neighbour: "BusStop"):
        return self.neighbours.get(neighbour, None)

    def __str__(self):
        return self.name + " connected to: " + ", ".join(
            [stop.name for stop in self.neighbours])
