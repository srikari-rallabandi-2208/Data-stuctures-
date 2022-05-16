//LeetCode - problem 2267

int visited[100][100][101] = {};

bool hasValidPath(vector<vector<char>>& grid, int i = 0, int j = 0, int bal = 0) {
    int m = grid.size(), n = grid[0].size();
    bal += grid[i][j] == '(' ? 1 : -1;
    if (bal < 0 || bal > (m + n) / 2 || visited[i][j][bal])
        return false;
    visited[i][j][bal] = true;
    if (i == m - 1 && j == n - 1 && bal == 0)
        return true;
    if (i < m - 1 && hasValidPath(grid, i + 1, j, bal))
        return true;
    if (j < n - 1 && hasValidPath(grid, i, j + 1, bal))
        return true;
    return false;
}
