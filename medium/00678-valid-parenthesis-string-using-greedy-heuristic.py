# https://leetcode.com/problems/valid-parenthesis-string/?envType=daily-question&envId=2024-04-07
# using greedy heuristic
class Solution:
    def checkValidString(self, s: str) -> bool:
        maxscore, minscore = 0,0
        for k in s:
            if k == "(":
                maxscore += 1
                minscore += 1
            elif k == ")":
                maxscore -= 1
                minscore -= 1
            else:
                maxscore += 1
                minscore -= 1
            if maxscore < 0:
                return False
            minscore = max(minscore, 0)
        return minscore == 0