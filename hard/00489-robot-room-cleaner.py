# https://leetcode.com/problems/robot-room-cleaner/
# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """
directions = [[1,0],[0,1],[-1,0],[0,-1]]
def solve(robot, x, y, direc, visited):
    robot.clean()
    visited.add((x,y))
    [nx,ny] = direc
    for _ in range(4):
        if (x + nx, y + ny) not in visited and robot.move():
            solve(robot, x + nx, y + ny, (nx,ny), visited)
        nx,ny = ny, -nx
        robot.turnRight()
    robot.turnRight()
    robot.turnRight()
    robot.move()
    robot.turnRight()
    robot.turnRight()
class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        solve(robot, 0, 0, (1,0), set())
        