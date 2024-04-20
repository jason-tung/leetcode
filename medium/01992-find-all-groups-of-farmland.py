# https://leetcode.com/problems/find-all-groups-of-farmland/submissions/1237200925/?envType=daily-question&envId=2024-04-20
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
class Solution:
        ret = []
            dfs(land, ni, nj, coord)
        if ni < len(land) and nj < len(land[0]) and land[ni][nj] == 1:
        ni,nj = d[0] + i,d[1] + j
    land[i][j] = 2
    for d in dirs:
    coord[2:] = [max(i, coord[2]), max(j, coord[3])]
def dfs(land, i, j, coord):
dirs = [[0,1],[1,0]]
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 1:
                    coord = [i,j,i,j]
                    dfs(land, i, j, coord)
                    ret.append(coord)
        return ret