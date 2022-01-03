from typing import List
'''
You are given a circular lock with three wheels,
each of which display the numbers 0 through 9 in order.
Each of these wheels rotate clockwise and counterclockwise.

In addition, the lock has a certain number of "dead ends",
meaning that if you turn the wheels to one of these combinations,
the lock becomes stuck in that state and cannot be opened.

Let us consider a "move" to be a rotation of a single wheel by one digit,
in either direction. Given a lock initially set to 000, a target combination,
and a list of dead ends, write a function that returns the minimum number of
moves required to reach the target state, or None if this is impossible.

This is a A* pathfinding algorthim over a 3d space,
where deadnodes are un-passable.
We will give them a value of 1.
'''


class WheelNode:
    def __init__(self, parent=None, position=None, value=0):
        self.parent: object
        self.position: List[int]

        self.parent = parent
        self.position = position

        self.value = value
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, __o: object) -> bool:
        return self.position == __o.position

    def __repr__(self) -> str:
        return f'({self.position[0]}, {self.position[1]})'

    def __lt__(self, __o: object):
        return self.f < __o.f

    def get_cost(self):
        return self.value

    def __hash__(self) -> int:
        return hash(repr(self))


def neighbors(
    node: WheelNode,
    deadEnds: List[WheelNode]
) -> WheelNode:
    pos = node.position
    # each node is connected to +- 1 in each
    # of the three wheel positions
    # +-1 mod 10
    # first wheel
    new_pos = [pos[0] + 1 % 10, pos[1], pos[2]]
    yield WheelNode(
        node,
        new_pos,
        1 if new_pos in deadEnds else 0
        )
    new_pos = [pos[0] - 1 % 10, pos[1], pos[2]]
    yield WheelNode(
        node,
        new_pos,
        1 if new_pos in deadEnds else 0
        )
    # second wheel
    new_pos = [pos[0], pos[1] + 1 % 10, pos[2]]
    yield WheelNode(
        node,
        new_pos,
        1 if new_pos in deadEnds else 0
        )
    new_pos = [pos[0], pos[1] - 1 % 10, pos[2]]
    yield WheelNode(
        node,
        new_pos,
        1 if new_pos in deadEnds else 0
        )
    # third wheel
    new_pos = [pos[0], pos[1], pos[2] + 1 % 10]
    yield WheelNode(
        node,
        new_pos,
        1 if new_pos in deadEnds else 0
        )
    new_pos = [pos[0], pos[1], pos[2] - 1 % 10]
    yield WheelNode(
        node,
        new_pos,
        1 if new_pos in deadEnds else 0
        )


def findPath(
    end: List[int],
    deadNodes: List[List[int]]
) -> List[List[int]]:

    startNode = WheelNode(None, [0, 0, 0])
    setattr(startNode, 'g', 0)
    setattr(startNode, 'h', 0)
    setattr(startNode, 'f', 0)

    endNode = WheelNode(None, end)
    setattr(endNode, 'g', 0)
    setattr(endNode, 'h', 0)
    setattr(endNode, 'f', 0)

    openList = []
    closedList = set()

    openList.append(startNode)

    while len(openList) > 0:
        openList.sort(reverse=False)
        currentNode = openList[0]
        openList.pop(0)
        closedList.add(currentNode)

        if currentNode == endNode:
            path = []
            current = currentNode
            while current is not None:
                path.append(getattr(current, 'position'))
                current = getattr(current, 'parent')
            return path[::-1]

        # Loop through children
        child: WheelNode
        for child in neighbors(currentNode, deadNodes):
            # check if the child is a dead node,
            # dead nodes have a value of 1
            if child.value != 0:
                continue
            # Child is on the closed list
            if child in closedList:
                continue

            # Create the f, g, and h values
            child.g = currentNode.g + 1
            # we do not have a h value
            child.h = 0
            child.f = child.g + child.h
            # Child is already in the open list
            if child in openList:
                position = openList.index(child)
                if openList[position].g > child.g:
                    openList.pop(position)
                    openList.append(child)
                continue
            # Add the child to the open list
            openList.append(child)


def calculateTurns(
    end: List[int],
    DeadNodes: List[List[int]]
) -> int:
    path = findPath(
        end,
        DeadNodes
    )
    # cost is the length of this path
    return len(path)
