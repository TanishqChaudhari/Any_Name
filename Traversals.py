from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        bfs_result = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                bfs_result.append(vertex)
                queue.extend(set(self.graph.get(vertex, [])) - visited)

        return bfs_result

    def dfs(self, start):
        visited = set()
        dfs_result = []

        def dfs_helper(vertex):
            visited.add(vertex)
            dfs_result.append(vertex)
            for neighbor in self.graph.get(vertex, []):
                if neighbor not in visited:
                    dfs_helper(neighbor)

        dfs_helper(start)
        return dfs_result

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(2, 6)
    g.add_edge(3, 7)
    g.add_edge(4, 7)
    g.add_edge(5, 8)
    g.add_edge(6, 8)

    start_vertex = 0
    print("BFS Traversal starting from vertex", start_vertex, ":", g.bfs(start_vertex))
    print("DFS Traversal starting from vertex", start_vertex, ":", g.dfs(start_vertex))