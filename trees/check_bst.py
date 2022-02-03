class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


def is_bst(node, lower_lim=None, upper_lim=None):
    if lower_lim is not None and node.value < lower_lim:
        return False
    if upper_lim is not None and upper_lim < node.value:
        return False

    is_left_bst = True
    is_right_bst = True
    if node.left:
        is_left_bst = is_bst(node.left, lower_lim, node.value)
    if is_left_bst and node.right:
        is_right_bst = is_bst(node.right, node.value, upper_lim)
    return is_left_bst and is_right_bst


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
