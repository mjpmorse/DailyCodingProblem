from typing import Tuple, List


class Node:

    def __init__(self, name: str) -> None:
        self.name = name
        self.left = None
        self.right = None
        self.visited = False

    def add_children(self, left: object, right: object) -> None:
        self.left = left
        self.right = right


def find(
        root: Node, level: int,
        max_level: List[int], res: List[str]):

    if root is not None:
        level += 1
        find(root.left, level, max_level, res)

        if level > max_level[0]:
            res[0] = root.name
            max_level[0] = level

        find(root.right, level, max_level, res)

    return res[0], max_level[0]


def deepest_node(root: Node) -> Tuple[str, int]:
    res = ['']
    max_level = [-1]

    res, max_level = find(root, 0, max_level, res)

    return res, max_level


if __name__ == '__main__':
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    b.add_children(d, None)
    a.add_children(b, c)
    print(deepest_node(a))
