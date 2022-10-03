//LeetCode - problem 68

    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        int start = 0, end = 0;
        vector<string> res;
        while (end < words.size()) {
            int len = 0, total = 0;
            while (end < words.size() && len + words[end].size() <= maxWidth) {
                len += words[end].size() + 1;
                total += words[end].size();
                ++end;
            }
            bool isLast = (end == words.size());
            res.push_back(justify(words, start, end, maxWidth - total, isLast));
            start = end;
        }
        return res;
    }
    
    string justify(const vector<string>& words, int start, int end, int space, bool isLast) {
        string line;
        if (!isLast) {
			int count = end - start - 1;  
            for (int i = start; i < end; ++i) {
                line += words[i];
                if (count > 0) {
                    int cur = space % count != 0? space/count + 1: space/count;
                    line.insert(line.end(), cur, ' ');
                    space -= cur;
                    --count;
                }
            }
        } else {
            for (int i = start; i < end; ++i) {
                line += words[i];
                if (space-- > 0) line.push_back(' ');
            }
        }
        if (space > 0) line.insert(line.end(), space, ' ');
        return line;
    }
