//LeetCode - problem 997 - graphs

int findJudge(int n, vector<vector<int>>& trust) {
        int outDeg[n+1],inDeg[n+1];
        memset(outDeg,0,sizeof(outDeg));
        memset(inDeg,0,sizeof(inDeg));
        int m=trust.size();
        for(int i=0;i<m;i++){
            outDeg[trust[i][0]]++;
            inDeg[trust[i][1]]++;
        }
        for(int i=1;i<=n;i++)if(outDeg[i]==0&&inDeg[i]==n-1)return i;
        return -1;
    }
