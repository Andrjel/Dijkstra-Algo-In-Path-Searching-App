from __future__ import annotations
from typing import Dict
from domain.bus_stop import BusStop


class LineMap:
    """Klasa reprezentująca linię autobusową jako graf. Wierzchołkami są przystanki,
    a krawędziami połączenia między nimi. Klasa zawiera słownik, w którym kluczem jest nazwa przystanku,
    a wartością obiekt klasy BusStop, tworząc w ten sposób graf.
    """
    def __init__(self):
        self.bus_stops: Dict[name, BusStop] = {}

    def add_vertex(self, new_name: str) -> None:
        """Dodaje wierzchołek do grafu. Jeśli wierzchołek o podanej nazwie już istnieje, to nic nie robi."""
        self.bus_stops.update({new_name: BusStop(new_name)})

    def get_vertex(self, name: str) -> BusStop:
        """Zwraca wierzchołek o podanej nazwie. Jeśli wierzchołek o podanej nazwie nie istnieje, to zwraca None."""
        return self.bus_stops.get(name, None)

    def get_vertices(self) -> list:
        """Zwraca listę nazw wszystkich wierzchołków grafu."""
        return list(self.bus_stops.keys())

    def add_edge(self, first_name: str, second_name: str, weight: int, line_num: str) -> None:
        """Dodaje krawędź między wierzchołkami o podanych nazwach. Jeśli któryś z wierzchołków nie istnieje,
        to rzuca wyjątek KeyError."""
        try:
            self.bus_stops[first_name].add_neighbour(second_name, weight)
            self.bus_stops[first_name].add_line_num(line_num)
        except KeyError:
            raise KeyError("Bus stop with name: " + first_name + " doesn't exist")

    def __iter__(self) -> iter:
        """Zwraca iterator po wszystkich wierzchołkach grafu. Przez co możemy korzystać z klasy LineMap w pętli for."""
        return iter(self.bus_stops.values())
