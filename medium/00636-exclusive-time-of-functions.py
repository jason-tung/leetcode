# https://leetcode.com/problems/exclusive-time-of-functions/
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack, last_command, last_start = [], None, 0
        times = [0] * n
        for k in logs:
            command = k.split(":")
            command = [int(command[0]), command[1], int(command[2])]
            if command[1] == "start":
                if last_command == "start":
                    times[stack[-1]] += command[2] - last_start
                # check if we had dead time we couldve been running using stack
                elif last_command == "end" and len(stack) > 0:
                    times[stack[-1]] += command[2] - last_start - 1
                stack.append(command[0])
            else:
                stack.pop()
                if last_command == "start":
                    times[command[0]] += command[2] - last_start + 1
                else:
                    times[command[0]] += command[2] - last_start
            [last_command, last_start] = command[1:]
        return times
        