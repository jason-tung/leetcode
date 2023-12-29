#https://leetcode.com/problems/binary-tree-inorder-traversal/description/
                cur = cur.left
            # no more left so try right
            else:
                last = stack.pop()
                r.append(last.val)
                cur = last.right
                stack.append(cur)
            if cur:
            # keep going down left if possible
        return r
        while cur or len(stack) > 0:
        stack = []