# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
    cur.right = helper(nums[med+1:])
    cur.left = helper(nums[:med])
    cur = TreeNode(val = nums[med])
        return None
    med = (len(nums)-1)//2
    if len(nums) == 0:
def helper(nums):
#         self.right = right
#         self.left = left
#         self.val = val
#     def __init__(self, val=0, left=None, right=None):
# class TreeNode:
# Definition for a binary tree node.
    return cur
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return helper(nums)
        
        