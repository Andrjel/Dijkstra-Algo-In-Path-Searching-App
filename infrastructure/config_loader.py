from domain.line_map import LineMap
import json
import os
import re


class ConfigLoader:
    """
    Klasa odpowiedzialna za wczytywanie konfiguracji z plików json
    """
    @staticmethod
    def load_config() -> LineMap:
        """Wczytanie konfiguracji z plików json"""
        # inicjalizacja mapy linii
        _line_map = LineMap()
        # iteracja po nazwach plików w folderze Lines
        for filename in os.listdir(r"C:\Users\GETAC\Desktop\Semestr 7\Projekty\p_2\Lines"):
            # wyrażenie regularne do określenia numeru linii
            regex = re.compile(r"\d+")
            line_number = regex.search(filename)[0]
            with open(r"C:\Users\GETAC\Desktop\Semestr 7\Projekty\p_2\Lines/" + filename) as data_file:
                # wczytanie danych z pliku json
                data = json.load(data_file)
            for _bus_stop in data:
                first_stop = _bus_stop
                second_stop = list(data[first_stop].keys())[0]
                weight = int(data[first_stop][second_stop])
                # dodanie wierzchołków i krawędzi do mapy linii
                if not _line_map.get_vertex(first_stop):
                    _line_map.add_vertex(first_stop)
                _line = [first_stop, second_stop, weight, line_number]
                _line_map.add_edge(*_line)
        return _line_map


if __name__ == "__main__":
    line_map = ConfigLoader.load_config()
    # for bus_stop in line_map:
    #     print(bus_stop)
