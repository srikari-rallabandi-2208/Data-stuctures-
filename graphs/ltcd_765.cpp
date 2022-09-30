//LeetCode - problem 765

class Solution {
    vector<int> parent;
public:

    int find(int x){
        if(parent[x]==x){
            return x;
        }
        parent[x] = find(parent[x]);
        return parent[x];
    }
    
    bool Union(int x, int y){
        int a = find(x);
        int b = find(y);
        if(a==b)return false;
        parent[a] = b;
        return true;
    }
    
    int minSwapsCouples(vector<int>& row) {
        parent.resize(row.size());
        
        for(int i=0;i<row.size();i+=2){
            parent[row[i]] = row[i];
            parent[row[i+1]] = row[i];
        }
        
        int counter = 0;
        for(int i=0;i<row.size();i+=2){
            if(Union(i,i+1)){
                counter++;
            }
        }
       return counter; 
    }
};
