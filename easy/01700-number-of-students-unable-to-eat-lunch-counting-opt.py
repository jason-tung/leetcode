# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/?envType=daily-question&envId=2024-04-08
# counting opt
# reduce from n^2 to n
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        co = 0
        for k in students:
            if k == 1:
                co += 1
        cz = len(students) - co
        for k in sandwiches:
            if k == 0:
                if cz == 0:
                    return co
                cz -= 1
            elif k == 1:
                if co == 0:
                    return cz
                co -= 1
        return cz + co
            