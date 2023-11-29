from typing import Dict


class BusStop:
    """Klasa Reprezentująca przystanek autobusowy. Przystanek jest reprezentowany przez nazwę, listę linii, które
    na nim się zatrzymują oraz słownik sąsiadów, gdzie kluczem jest obiekt BusStop, a wartością waga krawędzi
    pomiędzy tymi przystankami. Przystanek jest węzłem w grafie.
    """
    def __init__(self, name: str):
        self.__name = name
        self.__line_num = []
        self.neighbours: Dict[BusStop, int] = {}

    def add_neighbour(self, new_name: str, weight: int) -> None:
        """Dodaje sąsiada do słownika sąsiadów. Jeżeli sąsiad już istnieje, to aktualizuje jego wagę."""
        self.neighbours.update({BusStop(new_name): weight})

    @property
    def name(self) -> str:
        # getter
        return self.__name

    @property
    def line_num(self) -> list:
        # getter
        return self.__line_num

    def get_neighbours(self) -> Dict[BusStop, int]:
        """Zwraca słownik zawierający sąsiednie przystanki"""
        return self.neighbours

    def add_line_num(self, line_num: str) -> None:
        """Dodaje numer linii do listy numerów linii, które zatrzymują się na tym przystanku."""
        if line_num not in self.__line_num:
            self.__line_num.append(line_num)

    def get_weight(self, neighbour: "BusStop") -> int:
        """Zwraca wagę krawędzi pomiędzy tym przystankiem, a przystankiem podanym jako argument."""
        return self.neighbours.get(neighbour, None)

    def __str__(self):
        return self.name

