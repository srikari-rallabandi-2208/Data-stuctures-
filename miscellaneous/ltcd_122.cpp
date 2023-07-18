//LeetCode - problem 122

    int maxProfit(vector<int>& arr) {
        int profit=0;
        for(int i=0;i<arr.size()-1;i++){
            if(arr[i]<arr[i+1])
                profit+=(arr[i+1]-arr[i]);
        }
        return profit;
    }
