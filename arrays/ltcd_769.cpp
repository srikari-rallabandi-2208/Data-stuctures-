//LeetCode - problem 769

    int maxChunksToSorted(vector& arr) {
        int chunk = 0;
        int mx = arr[0];
        for(int i = 0; i< arr.size() ;i++){
            if(mx == i and arr[i] <= i){
                chunk++;
                if(i == arr.size() -1) break;
                mx = arr[i+1];
            }
            else{
                mx = max(mx , arr[i]);
            }
        }
        return chunk;
    }
