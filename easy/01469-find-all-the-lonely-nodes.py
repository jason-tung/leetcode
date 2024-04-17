# https://leetcode.com/problems/find-all-the-lonely-nodes/?envType=weekly-question&envId=2024-04-15
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        r = []
        def helper(node, isLonely):
            if isLonely:
                r.append(node.val)
            isLonely = True
            if node.left and node.right:
                isLonely = False
            helper(node.left, isLonely) if node.left else None
            helper(node.right, isLonely) if node.right else None
        helper(root, False)
        return r
            
            
            