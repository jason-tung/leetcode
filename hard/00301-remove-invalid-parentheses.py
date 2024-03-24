# https://leetcode.com/problems/remove-invalid-parentheses/
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ret = set()
        best = 0
        def dfs(s, i, cur_str, lc, rc):
            nonlocal best, ret
            if i == len(s):
                if lc == rc:
                    if len(cur_str) > best:
                        ret = set()
                        best = len(cur_str)
                    if len(cur_str) >= best:
                        ret.add(''.join(cur_str))
            else:
                if s[i] == "(":
                    cur_str.append("(")
                    dfs(s, i+1, cur_str, lc+1, rc)
                    cur_str.pop()
                    dfs(s, i+1, cur_str, lc, rc)
                elif s[i] == ")":
                    dfs(s, i+1, cur_str, lc, rc)
                    if lc > rc:
                        cur_str.append(")")
                        dfs(s, i+1, cur_str, lc, rc+1)
                        cur_str.pop()
                else:
                    cur_str.append(s[i])
                    dfs(s, i+1, cur_str, lc, rc)
                    cur_str.pop()
        dfs(s, 0, [], 0, 0)
        return list(ret)