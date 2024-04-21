# https://leetcode.com/problems/find-if-path-exists-in-graph/?envType=daily-question&envId=2024-04-21
            node = queue.pop()
        while queue:
        queue = deque([source])
            d[b].append(a)
            d[a].append(b)
            [a,b] = pair
        d = defaultdict(list)
        for pair in edges:
        visited[source] = True
            return True
        visited = [False] * n
        if source == destination:
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
            for dest in d[node]:
                if not visited[dest]:
                    if dest == destination:
                        return True
                    queue.appendleft(dest)
                    visited[dest] = True
        return False