from infrastructure.config_loader import ConfigLoader


class Dijkstra:
    def __init__(self, line_map):
        self.line_map = line_map

    def dijkstra(self, start, end):
        shortest_distance = {}
        predecessor = {}
        unseen_nodes = self.line_map.get_vertices()
        infinity = 9999999
        path = []
        # print(unseen_nodes)

        for node in unseen_nodes:
            shortest_distance[node] = infinity
        shortest_distance[start] = 0

        while unseen_nodes:
            min_distance_node = None
            for node in unseen_nodes:
                if min_distance_node is None:
                    min_distance_node = node
                elif shortest_distance[node] < shortest_distance[min_distance_node]:
                    min_distance_node = node

            for child_node, weight in self.line_map.get_vertex(min_distance_node).get_neighbours().items():
                if weight + shortest_distance[min_distance_node] < shortest_distance[str(child_node)]:
                    shortest_distance[str(child_node)] = weight + shortest_distance[min_distance_node]
                    predecessor[str(child_node)] = min_distance_node
            unseen_nodes.remove(min_distance_node)

        current_node = end
        while current_node != start:
            try:
                path.insert(0, current_node)
                current_node = predecessor[current_node]
            except KeyError:
                print("Path not reachable")
                break
        path.insert(0, start)
        return shortest_distance[end], path

    def get_route(self, start, end):
        shortest_distance: int
        path = []
        shortest_distance, path = self.dijkstra(start, end)
        route = []
        for stop_name in path:
            route.append(self.line_map.get_vertex(stop_name).line_num)
        print(shortest_distance)
        print(path)
        print(route)


def main():
    Dijkstra(ConfigLoader.load_config()).get_route("Zawadzkiego Kościół", "Turzyn Dworzec")
    Dijkstra(ConfigLoader.load_config()).get_route("Zawadzkiego Kościół", "Plac Rodła")
    Dijkstra(ConfigLoader.load_config()).get_route("Wita Stwosza", "Plac Rodła")


if __name__ == "__main__":
    main()
