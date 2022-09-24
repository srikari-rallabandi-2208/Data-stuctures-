//LeetCode - problem 2376

   int vec[1 << 10][10][2][2];
    int ans(string &s, int i, int m, int last, int b)
    {
        if (i == s.size())
        {
            return 1;
        }
        if (vec[m][i][last][b] != -1)
            return vec[m][i][last][b];

        int maxxx = b ? s[i] - '0' : 9;

        int total = 0;

        for (int j = 0; j <= maxxx; j++)
        {
            if (last == 0 && (m & (1 << j)))
                continue;
            m = m | (1 << j);
            total = total + ans(s, i + 1, m, last & (j == 0), b & (j == maxxx));
            m = m ^ (1 << j);
        }

        return vec[m][i][last][b] = total;
    }
    int numdub(int n)
    {
        string s = to_string(n);
        memset(vec, -1, sizeof(vec));
        int m = 0;
        return (n + 1) - ans(s, 0, m, 1, 1);
    }
    int countSpecialNumbers(int n)
    {
        int a = numdub(n);
        return n - a;
    }
