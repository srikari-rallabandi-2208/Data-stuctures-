//LeetCode - problem 2178 - Greedy Algo

    vector<long long> maximumEvenSplit(long long n) {
        if(n%2) 
            return {};

		vector<long long> ans;
        long long i = 2;
        long long crSum=0;
		
        while((crSum+i)<= n)
        {
            ans.push_back(i);
            crSum+=i;
            i+=2;
        }
		
		int sz = ans.size();
        ans[sz-1] += (n-crSum);
        return ans;
    }
