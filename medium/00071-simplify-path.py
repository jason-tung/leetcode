# https://leetcode.com/problems/simplify-path/
class Solution:
    def simplifyPath(self, path: str) -> str:
        i = 0
        path = path[1:].split("/")
        ret = ['']
        for k in path:
            if k != '':
                if k == '..':
                    if len(ret) > 1:
                        ret.pop()
                elif k != '.':
                    ret.append(k)
        return "/".join(ret) if len(ret) > 1 else "/"