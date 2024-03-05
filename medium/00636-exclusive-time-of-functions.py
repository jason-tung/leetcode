# https://leetcode.com/problems/exclusive-time-of-functions/
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack, last_command, last_start = [], None, 0
        times = [0] * n
        for k in logs:
            command = k.split(":")
            command = [int(command[0]), command[1], int(command[2])]
            # print(command, last_command)
            if command[1] == "start":
                # print("stk",stack)
                if last_command == "start":
                    times[stack[-1]] += command[2] - last_start
                elif last_command == "end" and len(stack) > 0:
                    times[stack[-1]] += command[2] - last_start - 1
                stack.append(command[0])
                
            else:
                stack.pop()
                times[command[0]] += command[2] - last_start + (1 if last_command == "start" else 0)
            [last_command, last_start] = command[1:]
            # print(times)
        return times
        