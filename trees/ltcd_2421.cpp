//LeetCode - problem 2421

#define fs first
#define sc second
class Solution {
public:
    int par[100005],mx[100005],sz[100005],cnt[100005];
    void make_set(){
        for(int i=0;i<100005;i++){
            par[i]=i;
            sz[i]=1;
        }
    }
    int find_par(int x){
        if(x==par[x]){
            return x;
        }
        return par[x]=find_par(par[x]);
    }
    int numberOfGoodPaths(vector<int>& a, vector<vector<int>>& edges) {
        vector<pair<int,pair<int,int>>>v;
        for(auto i:edges){
            v.push_back({max(a[i[0]],a[i[1]]),{i[0],i[1]}});
        }
        sort(v.begin(),v.end());
        make_set();
        int n=v.size();
        int ans=n+1;
        for(int i=0;i<n;i++){
            int op=v[i].fs;
            vector<bool>vis(n+1,false);
            while(i<v.size() && v[i].fs==op){
                int x=v[i].sc.fs;
                int y=v[i].sc.sc;
                int k1=0,k2=0;
                if(a[x]==op && !vis[x]){
                    k1++;
                }
                if(a[y]==op && !vis[y]){
                    k2++;
                }
                x=find_par(x);
                y=find_par(y);
                if(!vis[x]){
                    cnt[x]=0;
                    vis[x]=true;
                }
                if(!vis[y]){
                    cnt[y]=0;
                    vis[y]=true;
                }
                cnt[x]+=k1;
                cnt[y]+=k2;
                ans+=(cnt[x]*cnt[y]);
                if(sz[x]>=sz[y]){
                    sz[x]+=sz[y];
                    cnt[x]+=cnt[y];
                    par[y]=x;
                }else{
                    sz[y]+=sz[x];
                    cnt[y]+=cnt[x];
                    par[x]=y;
                }
                i++;
            }
            i--;
        }
        return ans;
    }
};
