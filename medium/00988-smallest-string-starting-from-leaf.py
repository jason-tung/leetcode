# https://leetcode.com/problems/smallest-string-starting-from-leaf/?envType=daily-question&envId=2024-04-17
                return ''
            ret.appendleft(node.val)
            if node.left
            if not node:
        def helper(node, ret):
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
                r = helper(node.left, ret)
                r = helper(node.right, ret)
            if node.right
            return ''.join(chr(k + ord('a')) for k in ret)
        return 