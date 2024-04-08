# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/?envType=daily-question&envId=2024-04-08
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i = 0
        j = 0
        anchor = len(students) - 1
        while j < len(sandwiches):
            i = i % len(students)
            if students[i] == sandwiches[j]:
                students[i] = -1
                j += 1
                anchor = i
            elif i == anchor:
                break
            i += 1
        return sum([1 for k in students if k != -1])