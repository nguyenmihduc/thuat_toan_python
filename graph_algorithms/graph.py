num_nodes1 = 5
edges1 = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]

num_nodes2 = 9
edges2 = [(0, 1), (0, 3), (1, 2), (2, 3), (4, 5), (4, 6), (5, 6), (7, 8)]

num_nodes3 = 9
edges3 = [
    (0, 1, 3),
    (0, 3, 2),
    (0, 8, 4),
    (1, 7, 4),
    (2, 7, 2),
    (2, 3, 6),
    (2, 5, 1),
    (3, 4, 1),
    (4, 8, 8),
    (5, 6, 8),
]

num_nodes4 = 5
edges4 = [(0, 1), (1, 2), (2, 3), (2, 4), (4, 2), (3, 0)]

num_nodes5 = 6
edges5 = [(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 4, 3), (4, 3, 4), (3, 5, 11)]


class Graph:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def __repr__(self):
        return "\n".join(
            ["{} : {}".format(n, neightbors) for n, neightbors in enumerate(self.data)]
        )

    def __str__(self):
        return self.__repr__()


class Graph2:
    def __init__(self, num_nodes, edges, directed=False, weighted=False):
        self.num_nodes = num_nodes
        self.directed = directed

        self.weighted = weighted
        self.data = [[] for _ in range(num_nodes)]
        self.weight = [[] for _ in range(num_nodes)]

        for edge in edges:
            if self.weighted:
                node1, node2, weight = edge
                self.data[node1].append(node2)
                self.weight[node1].append(weight)
                if not directed:
                    self.data[node2].append(node1)
                    self.weight[node2].append(weight)
            else:
                node1, node2 = edge
                self.data[node1].append(node2)
                if not directed:
                    self.data[node2].append(node1)

    def __repr__(self):
        result = ""
        if self.weighted:
            for i, (nodes, weights) in enumerate(zip(self.data, self.weight)):
                result += "{}: {}\n".format(i, list(zip(nodes, weights)))
        else:
            for i, nodes in enumerate(self.data):
                result += "{}: {}\n".format(i, nodes)
        return result

    def __str__(self):
        return self.__repr__()


def bfs(graph: Graph, root):
    queue = []
    discovered = [False] * len(graph.data)
    parent = [None] * len(graph.data)

    distance = [None] * len(graph.data)
    discovered[root] = True
    queue.append(root)

    distance[root] = 0
    idx = 0

    while idx < len(queue):
        # dequeue
        current = queue[idx]
        idx += 1

        # check all edges of current
        for node in graph.data[current]:
            if not discovered[node]:
                distance[node] = 1 + distance[current]
                parent[node] = current
                discovered[node] = True
                queue.append(node)

    return queue, distance, parent


def dfs(graph, root):
    stack = []
    discovered = [False] * len(graph.data)
    result = []

    stack.append(root)

    while len(stack) > 0:
        current = stack.pop()
        if not discovered[current]:
            discovered[current] = True
            result.append(current)

            for node in graph.data[current]:
                if not discovered[node]:
                    stack.append(node)

    return result, discovered, stack


graph1 = Graph2(num_nodes1, edges1)
# print(graph1)
# print(graph1.data)

graph2 = Graph2(num_nodes2, edges2)
# print(graph2)
# print(graph2.data)

graph3 = Graph2(num_nodes3, edges3, weighted=True)
# print(graph3)
# print(graph3.data)

graph4 = Graph2(num_nodes4, edges4, directed=True)
# print(graph4)
# print(graph4.data)

graph5 = Graph2(num_nodes5, edges5, weighted=True, directed=True)
# print(graph5)
# print(graph5.data)


# print(dfs(graph1, 3))
# print(bfs(graph1, 3))
# print(bfs(graph3, 3))


def update_distances(graph, current, distance, parent=None):
    """Update the distances of the current node's neighbors"""
    neighbors = graph.data[current]
    weights = graph.weight[current]
    for i, node in enumerate(neighbors):
        weight = weights[i]
        if distance[current] + weight < distance[node]:
            distance[node] = distance[current] + weight
            if parent:
                parent[node] = current


def pick_next_node(distance, visited):
    """Pick the next univisited node at the smallest distance"""
    min_distance = float("inf")
    min_node = None
    for node in range(len(distance)):
        if not visited[node] and distance[node] < min_distance:
            min_node = node
            min_distance = distance[node]
    return min_node


def shortest_path(graph, source, target):
    visited = [False] * len(graph.data)
    parent = [None] * len(graph.data)
    distance = [float("inf")] * len(graph.data)

    queue = []

    distance[source] = 0
    queue.append(source)
    idx = 0

    while idx < len(queue) and not visited[target]:
        current = queue[idx]
        visited[current] = True
        idx += 1

        #  update distances of all neighbors
        update_distances(graph, current, distance, parent)

        # find the first unvisited node with yhe smallest distance
        next_node = pick_next_node(distance, visited)
        if next_node:
            queue.append(next_node)

    print(">>> visited:", visited)
    print(">>> distance:", distance)
    print(">>> queue:", queue)
    print(">>> parent:", parent)

    return distance[target]


print(shortest_path(graph3, 2, 8))
# print(shortest_path(graph5, 0, 5))
