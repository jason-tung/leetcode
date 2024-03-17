# https://leetcode.com/problems/binary-search-tree-iterator/
# opt mem
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.queue = []
        self.appendAll(root)
    def next(self) -> int:
        r = self.queue.pop()
        self.appendAll(r.right)
        return r.val
        
    def hasNext(self) -> bool:
        return len(self.queue)
    def appendAll(self, node):
        while node:
            self.queue.append(node)
            node = node.left
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()