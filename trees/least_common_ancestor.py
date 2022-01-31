class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        if type(other) is type(self):
            return self.value == other.value
        return False


def lca(root, j, k):
    path_to_j = path_to_x(root, j)
    path_to_k = path_to_x(root, k)

    lca_to_return = None
    while path_to_j and path_to_k:
        j_pop = path_to_j.pop()
        k_pop = path_to_k.pop()
        if j_pop is k_pop:
            lca_to_return = j_pop
        else:
            break
    return lca_to_return


def path_to_x(root, x):
    if root is None:
        return None
    if root.value == x:
        return [root]
    left_path = path_to_x(root.left, x)
    if left_path is not None:
        left_path.append(root)
        return left_path
    right_path = path_to_x(root.right, x)
    if right_path is not None:
        right_path.append(root)
        return right_path
    return None


def create_tree(mapping, head_value):
    head = Node(head_value)
    nodes = {head_value: head}
    for key, value in mapping.items():
        nodes[value[0]] = Node(value[0])
        nodes[value[1]] = Node(value[1])
    for key, value in mapping.items():
        nodes[key].left = nodes[value[0]]
        nodes[key].right = nodes[value[1]]
    return head


