# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(root, val):
            nonlocal count

            if not root:
                return 

            if root.val >= val:
                count += 1

            dfs(root.left, max(root.val, val))
            dfs(root.right, max(root.val, val))

        dfs(root, root.val)
        return count