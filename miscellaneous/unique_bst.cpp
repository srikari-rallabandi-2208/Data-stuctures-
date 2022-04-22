//LeetCode - problem 96 - DP

int numTrees(int n) {
        double prod=1.0;
        for(double i=2*n,j=n;i>n+1,j>1;i-=1,j-=1) prod*=(i/j);
        return round(prod);
    }
