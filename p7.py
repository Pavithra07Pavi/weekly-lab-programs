from collections import deque

# Tree representation (Adjacency List)
tree = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}

# Breadth-First Search (BFS)
def bfs(tree, root):
    visited = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        visited.append(node)

        for child in tree[node]:
            queue.append(child)

    return visited


# Depth-First Search (DFS)
def dfs(tree, node, visited):
    visited.append(node)

    for child in tree[node]:
        dfs(tree, child, visited)

    return visited


# Main execution
if __name__ == "__main__":
    print("BFS:", *bfs(tree, 1))
    print("DFS:", *dfs(tree, 1, []))
