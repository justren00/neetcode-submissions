# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(root, maxim):
            nonlocal res 

            if not root:
                return 

            if root.val >= maxim:
                res += 1
                maxim = root.val

            dfs(root.left, maxim)
            dfs(root.right, maxim)

        dfs(root, float('-inf'))
        return res
            