# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        r = []
        stack = [root]
        cur = root
        prev = TreeNode(val=-1)
        while cur or len(stack) > 0:
            # print(cur)
            # print([k.val for k in stack])
            # print(r)
            # print("prev", prev)
            # check we neither kid was backtracked
            if cur and cur.left and cur.left != prev and cur.right != prev:
                # print("proc")
                stack.append(cur.left)
                cur = cur.left
            else:
                # print("proc2")
                # add a check because we need to visit the node twice - once to 
traverse the right tree and once to pop the value off
                # checkc but dont pop off because we will need to go back to it
                if len(stack) > 0: