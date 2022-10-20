//LeetCode - problem 786

vector kthSmallestPrimeFraction(vector& nums, int k) {
    double low=0,high=1;
    int n=nums.size();
    while(low<=high){
        double mid=(low+high)/2;
        double maxf=0.0;
        int p,q;
        int total=0;
        int j=1;
        for(int i=0;i<n-1;i++){
            while(j<n && (double)nums[i]/(double)nums[j]>mid){
                j++;
            }
            total+=(n-j);
            if(j==n){
                break;
            }
            double frac=(double)nums[i]/(double)nums[j];
            if(frac>=maxf){
                maxf=frac;
                p=i;
                q=j;
                
            }
        }
        if(total==k){
            return {nums[p],nums[q]};
        }
        else if(total>k){
            high=mid;
        }
        else{
            low=mid;
        }
        
    }
    return {};
}
