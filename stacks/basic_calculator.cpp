//LeetCode - problem 224

    int helper(string s, int &i) {
        char pre_char = '+';
        long long now = 0;
        int ret = 0;

        for(; i<s.size(); i++) {
            if(s[i] == ' ')
                continue;
            if('0' <= s[i] && s[i] <= '9')
                now = now*10 + s[i] - '0';
            else {
                if(s[i] == '(')
                    now = helper(s, ++i);

                if(pre_char == '+')
                    ret += now;
                else if(pre_char == '-')
                    ret -= now;
                    
                if(i < s.size() && s[i] == ')') {
                    i++;
                    return ret;
                }
                
                pre_char = s[i];
                now = 0;
            }
        }

        return ret;
    }

    int calculate(string s) {
        s.push_back('#');
        int i = 0;
        return helper(s, i);
    }
