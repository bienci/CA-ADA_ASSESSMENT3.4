
from collections import deque

# ==========================================
# ASSESSMENT 3.3: NON-LINEAR DATA STRUCTURES
# Name: CANADA
# ==========================================


# ==========================================
# PART 1: GRAPH (BFS AND DFS)
# ==========================================

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


# ==========================================
# PART 2: BINARY TREE (BFS AND DFS)
# ==========================================

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree():
    """Binary Tree for CANADA."""
    root = TreeNode("C")
    root.left, root.right = TreeNode("A"), TreeNode("N")
    root.left.left, root.left.right = TreeNode("A"), TreeNode("D")
    root.right.left = TreeNode("A")

    return root


def tree_bfs(root):
    """Level-Order Traversal (BFS)."""
    order = []

    if root is None:
        return order

    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        order.append(node.value)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return order


def tree_dfs(node, order=None):
    """Preorder Traversal (DFS)."""
    if order is None:
        order = []

    if node is None:
        return order

    order.append(node.value)

    tree_dfs(node.left, order)
    tree_dfs(node.right, order)

    return order


# ==========================================
# MAIN PROGRAM
# ==========================================

if __name__ == "__main__":

    # Display Graph
    graph = build_graph()

    print("===================================")
    print("       CANADA GRAPH")
    print("===================================")
    print("Adjacency List:")

    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")

    print("\nBFS:", " -> ".join(graph_bfs(graph, "C")))
    print("DFS:", " -> ".join(graph_dfs(graph, "C")))

    # Display Binary Tree
    root = build_tree()

    print("\n===================================")
    print("       CANADA BINARY TREE")
    print("===================================")

    print("BFS (Level-Order):", " -> ".join(tree_bfs(root)))
    print("DFS (Preorder):   ", " -> ".join(tree_dfs(root)))

    print("\n===================================")
    print("          PROGRAM END")
    print("===================================")
