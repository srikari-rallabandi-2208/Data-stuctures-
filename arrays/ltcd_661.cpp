//LeetCode - problem 661

    vector<vector<int>> imageSmoother(vector<vector<int>>& img) {
        int n = img.size();
        int m = img[0].size();
        vector<vector<int>> res = img;
        
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                float sum = img[i][j];
                int k = 1;
                
                if(i - 1 >= 0){
                    k++;
                    sum += img[i - 1][j];
                    if(j - 1 >= 0){
                        k++;
                        sum += img[i - 1][j - 1];
                    }
                    if(j + 1 < m){
                        k++;
                        sum += img[i - 1][j + 1];
                    }
                }
                if(i + 1 < n){
                    k++;
                    sum += img[i + 1][j];
                    if(j - 1 >= 0){
                        k++;
                        sum += img[i + 1][j - 1];
                    }
                    if(j + 1 < m){
                        k++;
                        sum += img[i + 1][j + 1];
                    }
                }
                if(j - 1 >= 0){
                    k++;
                    sum += img[i][j - 1];
                }
                if(j + 1 < m){
                    k++;
                    sum += img[i][j + 1];
                }
                res[i][j] = (int)(sum / k);
            }
        }
        return res;
    }
