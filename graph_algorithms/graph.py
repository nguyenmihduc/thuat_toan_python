num_nodes = 5
edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]

num_nodes3 = 9
edges3 = [(0, 1), (0, 3), (1, 2), (2, 3), (4, 5), (4, 6), (5, 6), (7, 8)]


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


graph1 = Graph(num_nodes, edges)
print(graph1)
print(graph1.data)

graph3 = Graph(num_nodes3, edges3)
# print(graph3)
# print(graph3.data)


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


# print(bfs(graph1, 3))
# print(bfs(graph3, 3))


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


print(dfs(graph1, 3))
