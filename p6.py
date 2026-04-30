# Tree Node Definition
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []


# Depth-Limited Search (DLS)
def depth_limited_search(node, depth_limit, current_depth=0, visited=None):
    if visited is None:
        visited = []

    if node is None:
        return visited

    # Visit current node
    visited.append(node.value)

    # Stop if depth limit reached
    if current_depth == depth_limit:
        return visited

    # Recur for children
    for child in node.children:
        depth_limited_search(child, depth_limit, current_depth + 1, visited)

    return visited


# Iterative Deepening DFS (IDDFS)
def iterative_deepening_dfs(root, max_depth):
    for depth in range(max_depth + 1):
        visited = depth_limited_search(root, depth)
        print(f"Depth Limit {depth}: Visited nodes {visited}")


# ----------------------------
# Build Example Tree
#        1
#       / \
#      2   3
#     /|   |\
#    4 5   6 7
# ----------------------------

root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

root.children = [node2, node3]
node2.children = [node4, node5]
node3.children = [node6, node7]


# Run DLS
print("DLS Visit Order:", depth_limited_search(root, 2))

# Run IDDFS
iterative_deepening_dfs(root, 2)
