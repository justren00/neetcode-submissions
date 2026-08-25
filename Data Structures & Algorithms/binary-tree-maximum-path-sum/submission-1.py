# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maximum = -float('inf')

        def dfs(root):
            nonlocal maximum

            if not root: 
                return 0

            left_subtree = dfs(root.left) + root.val
            right_subtree = dfs(root.right) + root.val
            middle_subtree = left_subtree + right_subtree - root.val 

            maximum = max(maximum, max(left_subtree, right_subtree, middle_subtree)) 

            return max(0, max(left_subtree, right_subtree))

        dfs(root)
        return maximum
            
