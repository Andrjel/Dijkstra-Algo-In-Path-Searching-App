from __future__ import annotations
from typing import Dict
from domain.bus_stop import BusStop


class LineMap:
    def __init__(self):
        self.bus_stops: Dict[name, BusStop] = {}

    def add_vertex(self, new_name: str) -> None:
        self.bus_stops.update({new_name: BusStop(new_name)})

    def get_vertex(self, name: str) -> BusStop:
        return self.bus_stops.get(name, None)

    def add_edge(self, first_name: str, second_name: str, weight: int) -> None:
        try:
            self.bus_stops[first_name].add_neighbour(second_name, weight)
        except KeyError:
            raise KeyError("Bus stop with name: " + first_name + " doesn't exist")

    def __iter__(self) -> iter:
        return iter(self.bus_stops.values())
