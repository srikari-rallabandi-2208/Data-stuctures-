//LeetCode - problem 2528

    bool isPowerable(vector<int> stations, long long minPower, int k, int r) {
        int start = -1*r;
        int end = r;
        int n = stations.size();
        
        long long current_pow = 0;
        for(int i=0; i<=r && i<n; i++){
            current_pow += stations[i];
        }
        
        int mid = 0;
        while(mid<n) {
            if(current_pow < minPower) {
                long long diff = minPower - current_pow;
                if(diff>k)return false;
                k -= diff;
                stations[min(mid+r, n-1)] += diff;
            }
            current_pow = max(current_pow, minPower);
            current_pow -= start>=0?stations[start]:0;
            current_pow += end<=n-2?stations[end+1]:0;
            start++;
            end++;
            mid++;
        }
        
        return true;
    }
    long long maxPower(vector<int>& stations, int r, int k) {
     
        long long start = 0;
        long long end = LONG_LONG_MAX;
        long long maxPow = 0;
        
        while(start<=end) {
            long long mid = (start + end)/2;
            if(isPowerable(stations, mid, k, r)) {
                start = mid+1;
                maxPow = max(maxPow, mid);
            }else {
                end = mid-1;
            }
        }
        
        return maxPow;
        
    }
