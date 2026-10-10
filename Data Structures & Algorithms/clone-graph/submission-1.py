"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}

        def cloneNode(node):
            if not node:
                return None

            if node in clones:
                return clones[node]

            clones[node] = Node(node.val, [])

            for neighbor in node.neighbors:
                clone = cloneNode(neighbor)
                clones[node].neighbors.append(clone)

            return clones[node]


        return cloneNode(node)
                