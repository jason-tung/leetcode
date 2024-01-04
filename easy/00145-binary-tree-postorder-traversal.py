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
        # None has an issue with non-existing nodes haha
        prev = TreeNode(val=-1)
        while cur or len(stack) > 0:
            # check we neither kid was backtracked
            if cur and cur.left and cur.left != prev and cur.right != prev:
                stack.append(cur.left)
                cur = cur.left
            else:
                # add a check because we need to visit the node twice - once to # traverse the right tree 
and once to pop the value off
                if len(stack) > 0:
                    backtrack = stack[-1]
                    if backtrack.right and backtrack.right != prev:
                        cur = backtrack.right
                        stack.append(cur)
                    elif cur == None:
                        cur = backtrack
                    else:
                        r.append(cur.val)
                        prev = cur
                        stack.pop()
                        cur = None
                else:
                    r.append(cur.val)
                    return r
        return r