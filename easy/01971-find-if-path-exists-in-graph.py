# https://leetcode.com/problems/find-if-path-exists-in-graph/?envType=daily-question&envId=2024-04-21
        visited = set([source])
        queue = deque([source])
        edges = set([(k[0],k[1]) for k in edges])
        while queue:
                    if (node, dest) in edges or (dest, node) in edges:
            node = queue.pop()
                        queue.appendleft(dest)
                        if dest == destination:
                            return True
            for dest in range(n):
                if dest not in visited:
        if source == destination:
            return True
                        visited.add(dest)
        return False
            # print(node)
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool: