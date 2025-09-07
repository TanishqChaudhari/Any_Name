"""Graph traversal implementation using BFS and DFS."""

from collections import deque


class Graph:
    """Graph class supporting BFS and DFS traversals."""

    def __init__(self):
        """Initialize an empty graph."""
        self.graph = {}

    def add_edge(self, u_node, v_node):
        """Add a directed edge from u_node to v_node."""
        if u_node not in self.graph:
            self.graph[u_node] = []
        self.graph[u_node].append(v_node)

    def bfs(self, start):
        """Perform Breadth-First Search starting from the given node."""
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
        """Perform Depth-First Search starting from the given node."""
        visited = set()
        dfs_result = []

        def dfs_helper(vertex):
            """Recursive DFS helper function."""
            visited.add(vertex)
            dfs_result.append(vertex)
            for neighbor in self.graph.get(vertex, []):
                if neighbor not in visited:
                    dfs_helper(neighbor)

        dfs_helper(start)
        return dfs_result


if __name__ == "__main__":
    GRAPH = Graph()
    GRAPH.add_edge(0, 1)
    GRAPH.add_edge(0, 2)
    GRAPH.add_edge(1, 3)
    GRAPH.add_edge(1, 4)
    GRAPH.add_edge(2, 5)
    GRAPH.add_edge(2, 6)
    GRAPH.add_edge(3, 7)
    GRAPH.add_edge(4, 7)
    GRAPH.add_edge(5, 8)
    GRAPH.add_edge(6, 8)

    START_VERTEX = 0
    print("BFS Traversal starting from vertex", START_VERTEX, ":", GRAPH.bfs(START_VERTEX))
    print("DFS Traversal starting from vertex", START_VERTEX, ":", GRAPH.dfs(START_VERTEX))
