//LeetCode - problem 385

class Solution {
    NestedInteger parse(const string &s, int & pos)
    {
        if (s[pos] == '[')
            return parseList(s, pos);
        return parseNum(s, pos);
    }
    NestedInteger parseNum(const string &s, int & pos)
    {
        int num = 0;
        int sign = s[pos] == '-' ? -1 : 1;
        if (s[pos] == '-' || s[pos] == '+')
            pos ++;
        for (;pos < s.size() && isdigit(s[pos]); pos ++)
            num = num * 10 + s[pos] - '0';
        return NestedInteger(sign * num);
    }
    NestedInteger parseList(const string &s, int &pos)
    {
        NestedInteger ni;
        while (s[pos] != ']')
        {
            pos ++;                   
            if (s[pos] == ']') break; 
            ni.add(parse(s, pos));
        }
        pos ++;                       
        return ni;
    }
public:
    NestedInteger deserialize(const string &s) {
        int pos = 0;
        return parse(s, pos);
    }
};
