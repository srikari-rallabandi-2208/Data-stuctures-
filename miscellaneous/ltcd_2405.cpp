//LeetCode - problem 2405

    int partitionString(string s) {
        
        int ans = 1;
        
        int i = 0 , n = s.size();
        string temp = "";
        while( i < n)
        {
            if(temp.find(s[i]) == string::npos)
            { 
                // cout<<temp<<endl;
                temp += s[i++];
            }
            else
            {
                cout<<temp<<endl;
                ans++;
                temp = "";
                temp+=s[i++];
            }
        }
        return ans;
    }
