# https://leetcode.com/problems/find-if-path-exists-in-graph/?envType=daily-question&envId=2024-04-21
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        visited = [False] * n
        visited[source] = True
        d = defaultdict(list)
        for pair in edges:
            [a,b] = pair
            d[a].append(b)
            d[b].append(a)
        queue = deque([source])
        while queue:
            node = queue.pop()
            for dest in d[node]:
                if not visited[dest]:
                    if dest == destination:
                        return True
                    queue.appendleft(dest)
                    visited[dest] = True
        return False