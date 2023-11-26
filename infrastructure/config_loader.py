from domain.line_map import LineMap
import json
import os


class ConfigLoader:
    @staticmethod
    def load_config() -> LineMap:
        _line_map = LineMap()
        for filename in os.listdir(r"C:\Users\GETAC\Desktop\Semestr 7\Projekty\p_2\Lines"):
            print(filename)
            with open(r"C:\Users\GETAC\Desktop\Semestr 7\Projekty\p_2\Lines/" + filename) as data_file:
                data = json.load(data_file)
            for _bus_stop in data:
                first_stop = _bus_stop
                second_stop = list(data[first_stop].keys())[0]
                weight = data[first_stop][second_stop]
                if not _line_map.get_vertex(first_stop):
                    _line_map.add_vertex(first_stop)
                _line = [first_stop, second_stop, weight]
                _line_map.add_edge(*_line)
        return _line_map


if __name__ == "__main__":
    line_map = ConfigLoader.load_config()
    for bus_stop in line_map:
        print(bus_stop)
