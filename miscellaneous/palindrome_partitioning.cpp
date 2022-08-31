//LeetCode - problem 1278

    int dp[101][101][101];
    int check(string s,int i,int j)
    {
        if(i>j) return 1000;
        int ans=0;
        while(i<j)
        {
            if(s[i]!=s[j])
                ans++;
            i++;j--;
        }
        return ans;
    }
    int solve(string s,int k,int i,int j)
    {
        if(i>j) return k<=0?0:1000;
        if(j-i+1==k) return dp[i][j][k]=0;
        if(j-i+1<k) return 1000;
        if(k==1) return dp[i][j][k]=check(s,i,j);
        if(dp[i][j][k]!=-1) return dp[i][j][k];
        int ans=1000;
        for(int x=i;x<j;x++)
        {
            int a=solve(s,1,i,x);
            int b=solve(s,k-1,x+1,j);
            ans=min(ans,a+b);
        }
        return dp[i][j][k]=ans;
    }
    int palindromePartition(string s, int k) {
        memset(dp,-1,sizeof(dp));
        return solve(s,k,0,s.size()-1);
    }
