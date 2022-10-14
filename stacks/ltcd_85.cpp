//LeetCode - problem 85

class Solution { 
    int kadane(vector<int> &arr,int &up,int &down,int &n){
        int max_sum=INT_MIN,max_sum_end = 0;
        for(int i=0;i<n;i++){
            max_sum_end +=arr[i];
            if(max_sum_end<arr[i]){
                max_sum_end = arr[i];
                up=i;
            }
            if(max_sum<max_sum_end){
                max_sum = max_sum_end;
                down = i;
            }
        }
        return max_sum;
    }
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        int cursum = 0, maxsum = 0,left=0,right=0,up=0,down=0;
        int row = matrix.size(),col = matrix[0].size();
        const int inf = -(row*col); 
        for(int l=0;l<col;l++){
            vector<int> temp(row);
            for(int r=l;r<col;r++){
                for(int i=0;i<row;i++){
                    temp[i]+=matrix[i][r]=='0'?inf:1;
                }
                cursum = kadane(temp,up,down,row);
                if(maxsum<cursum){
                    maxsum = cursum;
                    left = l;
                    right =r;
                }
            }
        }
        return maxsum;
    }
};
