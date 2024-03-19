# https://leetcode.com/problems/task-scheduler/?envType=daily-question&envId=2024-03-19
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        max_ele, max_count = [], 0
        for k in tasks:
            if k not in d:
                d[k] = 1
            else:
                d[k] += 1
            if d[k] > max_count:
                max_ele, max_count = set(k), d[k]
            if d[k] == max_count:
                max_ele.add(k)
        return max(len(max_ele) * max_count + (max_count - 1) * (n - len(max_ele) + 1), len(tasks))