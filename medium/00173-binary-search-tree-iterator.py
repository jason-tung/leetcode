# https://leetcode.com/problems/binary-search-tree-iterator/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.queue = deque()
        def iter(root):
            if root:
                iter(root.left) if root.left else None
                self.queue.appendleft(root.val) 
                iter(root.right) if root.right else None
        iter(root)
    def next(self) -> int:
        return self.queue.pop()
        
    def hasNext(self) -> bool:
        return len(self.queue)
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()