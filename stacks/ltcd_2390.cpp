//LeetCode - problem 2390

string removeStars(string s) {
        string res;
        for (char c : s)
            if (c == '*')
                res.pop_back();
            else
                res += c;
        return res;
    }
