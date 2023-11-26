from domain.line_map import LineMap
import json
import os


class ConfigLoader:
    @staticmethod
    def load_config() -> LineMap:
        line_map = LineMap()
        for filename in os.listdir(r"C:\Users\GETAC\Desktop\Semestr 7\Projekty\p_2\Lines"):
            print(filename)
            with open(r"C:\Users\GETAC\Desktop\Semestr 7\Projekty\p_2\Lines/" + filename) as data_file:
                data = json.load(data_file)
            for bus_stop in data:
                first_stop = bus_stop
                second_stop = list(data[first_stop].keys())[0]
                weight = data[first_stop][second_stop]
                if not line_map.get_vertex(first_stop):
                    line_map.add_vertex(first_stop)
                if not line_map.get_vertex(second_stop):
                    line_map.add_vertex(second_stop)
                line_to = [first_stop, second_stop, weight]
                line_from = [second_stop, first_stop, weight]
                line_map.add_edge(*line_to)
                line_map.add_edge(*line_from)
        return line_map


if __name__ == "__main__":
    line_map = ConfigLoader.load_config()
    for bus_stop in line_map:
        print(bus_stop)
