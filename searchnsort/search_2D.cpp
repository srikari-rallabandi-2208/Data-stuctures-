//leetcode problem 74 - search a 2D matrix

bool searchMatrix(vector<vector<int>>& a, int x) {
        int n=a.size();
        if(n==0) return 0;
        int m=a[0].size();
        int l=0,h=n*m-1;
        while(l<=h) {
            int mid=(l+h)/2;
            int r=mid/m;
            int c=mid%m;
            if(a[r][c]==x) return 1;
            if(a[r][c]>x) h=mid-1;
            else l=mid+1;
        }
        return 0;
    }
