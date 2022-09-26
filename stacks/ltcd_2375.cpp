//LeetCode - problem 2375

    bool check(vector<int> &ans,string &p){
        int n=p.size();
        for(int i=0;i<n;i++){
            if(p[i]=='I' && (ans[i])>=(ans[i+1]))return false;
            else if(p[i]=='D' && (ans[i])<=(ans[i+1]))return false;
        }
        return true;
    }
    string smallestNumber(string p) {
        int n=p.size();
        vector<int> ans;
        for(int i=1;i<=n+1;i++){
            ans.push_back(i);
        }
        do{
            if(check(ans,p))break;
        }while(next_permutation(ans.begin(),ans.end()));
        
        string temp;
        for(auto it:ans)temp.push_back(it+'0');
        return temp;
    }
