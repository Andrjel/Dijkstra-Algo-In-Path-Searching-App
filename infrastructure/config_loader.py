from domain.line_map import LineMap
import json
import os
import re


class ConfigLoader:
    @staticmethod
    def load_config() -> LineMap:
        _line_map = LineMap()
        for filename in os.listdir(r"C:\Users\GETAC\Desktop\Semestr 7\Projekty\p_2\Lines"):
            # print(filename)
            regex = re.compile(r"\d+")
            line_number = regex.search(filename)[0]
            # print(line_number)
            with open(r"C:\Users\GETAC\Desktop\Semestr 7\Projekty\p_2\Lines/" + filename) as data_file:
                data = json.load(data_file)
            for _bus_stop in data:
                first_stop = _bus_stop
                second_stop = list(data[first_stop].keys())[0]
                weight = int(data[first_stop][second_stop])
                if not _line_map.get_vertex(first_stop):
                    _line_map.add_vertex(first_stop, line_number)
                _line = [first_stop, second_stop, weight, line_number]
                _line_map.add_edge(*_line)
        return _line_map


if __name__ == "__main__":
    line_map = ConfigLoader.load_config()
    # for bus_stop in line_map:
    #     print(bus_stop)
