from infrastructure.config_loader import ConfigLoader


class Dijkstra:
    """
    Klasa implementująca algorytm Dijkstry
    """
    def __init__(self, line_map):
        self.line_map = line_map

    def __dijkstra(self, start, end):
        """Algorytm dijkstry"""

        # Inicjalizacja struktur danych
        shortest_distance = {}
        predecessor = {}
        unseen_nodes = self.line_map.get_vertices()
        infinity = 9999999
        path = []

        # Inicjalizacja odległości do wszystkich wierzchołków jako nieskończoność
        for node in unseen_nodes:
            shortest_distance[node] = infinity
        # Inicjalizacja odległości do wierzchołka startowego jako 0
        shortest_distance[start] = 0

        # Główna pętla algorytmu Dijkstry
        while unseen_nodes:
            min_distance_node = None
            for node in unseen_nodes:
                if min_distance_node is None:
                    min_distance_node = node
                elif shortest_distance[node] < shortest_distance[min_distance_node]:
                    min_distance_node = node

            # Aktualizacja najkrótszych odległości dla sąsiadów aktualnego wierzchołka
            for child_node, weight in self.line_map.get_vertex(min_distance_node).get_neighbours().items():
                if weight + shortest_distance[min_distance_node] < shortest_distance[str(child_node)]:
                    shortest_distance[str(child_node)] = weight + shortest_distance[min_distance_node]
                    predecessor[str(child_node)] = min_distance_node
            unseen_nodes.remove(min_distance_node)

        # Odtworzenie ścieżki do końcowego wierzchołka od początkowego
        current_node = end
        while current_node != start:
            try:
                path.insert(0, current_node)
                current_node = predecessor[current_node]
            except KeyError:
                print("Path not reachable")
                break
        path.insert(0, start)
        return path

    def get_route(self, start, end):
        # inicjalizacja zmiennej path
        path = []

        # wywołanie algorytmu dijkstry
        path = self.__dijkstra(start, end)
        route = []

        # zamiana nazw przystanków na numery linii
        for stop_name in path:
            route.append(self.line_map.get_vertex(stop_name).line_num)

        # Wybranie odpowiedniej lini
        final_route = self.get_final_route(route)

        # wyliczenie odległości między przystankami
        path_distance = self.calc_distance(path)

        # Przygotowanie wynikowej struktury danych z informacjami o trasie
        result = []
        for idx, stop_name in enumerate(path, start=0):
            if idx != len(path) - 1:
                result.append([stop_name, path_distance[idx], final_route[idx]])
                if idx < len(path) -2 and final_route[idx] != final_route[idx + 1]:
                    result.append([path[idx + 1], 1, "Przesiadka " + final_route[idx] + " -> " + final_route[idx + 1]])
                continue
            result.append([stop_name])

        return result

    def calc_distance(self, path):
        """Obliczenie odległości między przystankami"""
        path_distance = []
        for idx, stop_name in enumerate(path, start=0):
            if idx == len(path) - 1:
                break
            neighbours = self.line_map.get_vertex(stop_name).get_neighbours()
            for neighbour, weight in neighbours.items():
                if neighbour.name == path[idx + 1]:
                    path_distance.append(weight)
                    break
        return path_distance

    def get_final_route(self, route):
        """Wybranie ostatecznej linii autobusowej, którą należy podążać"""
        final_route = []
        for idx, lines_num in enumerate(route, start=0):
            if idx == len(route) - 1:
                break
            for line in lines_num:
                if line in route[idx + 1]:
                    final_route.append(line)
                    break
        return final_route


def main():
    Dijkstra(ConfigLoader.load_config()).get_route("Zawadzkiego Kościół", "Turzyn Dworzec")
    Dijkstra(ConfigLoader.load_config()).get_route("Zawadzkiego Kościół", "Plac Rodła")
    Dijkstra(ConfigLoader.load_config()).get_route("Wita Stwosza", "Plac Rodła")
    Dijkstra(ConfigLoader.load_config()).get_route("Plac Rodła", "Wita Stwosza")
    Dijkstra(ConfigLoader.load_config()).get_route("Turkusowa", "Kołłątaja")
    Dijkstra(ConfigLoader.load_config()).get_route("Plac Rodła", "Podbórz")


if __name__ == "__main__":
    main()
