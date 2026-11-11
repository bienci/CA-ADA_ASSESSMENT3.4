
from collections import deque

"""
Assessment 3.3: Non-linear Data Structures
Diagram 1: CANADA Graph (BFS and DFS)
"""

# Each letter has a unique node ID.
NAME_ORDER = ["C", "A", "N", "A2", "D", "A3"]

EDGES = [
    ("C", "A"),
    ("C", "N"),
    ("A", "N"),
    ("N", "A2"),
    ("A2", "D"),
    ("D", "A3")
]


def build_graph():
    """Build an adjacency list."""
    graph = {node: [] for node in NAME_ORDER}

    for u, v in EDGES:
        graph[u].append(v)
        graph[v].append(u)

    for node in graph:
        graph[node].sort(key=NAME_ORDER.index)

    return graph


def graph_bfs(graph, start):
    """Algorithm A: Breadth-First Search."""
    queue = deque()
    visited = []
    order = []

    queue.append(start)
    visited.append(start)

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

    return order


def graph_dfs(graph, start):
    """Algorithm B: Depth-First Search."""
    stack = []
    visited = []
    order = []

    stack.append(start)

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.append(node)
        order.append(node)

        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)

    return order


if __name__ == "__main__":
    graph = build_graph()

    print("=== Diagram 1: CANADA Graph ===")
    print("Adjacency list:")

    for node, neighbors in graph.items():
        print(f"  {node}: {neighbors}")

    print("BFS:", " -> ".join(graph_bfs(graph, "C")))
    print("DFS:", " -> ".join(graph_dfs(graph, "C")))
