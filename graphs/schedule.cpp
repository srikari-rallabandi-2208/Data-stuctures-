//LeetCode - problem 207 - graphs

class Solution {
public:
    bool cycle(vector<vector<int>>& graph,bool b1[],bool b2[],int i){
        b1[i]=true;  b2[i]=true;
        for(auto val:graph[i]){
            if(!b1[val]){
                if(!cycle(graph,b1,b2,val))  return false; }   
            else if(b2[val])     
                return false;
        }
        b2[i]=false;
        return true;
    }
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> graph(numCourses+1);
        //create a graph first from the given pairs
        for(auto v:prerequisites){
            graph[v[1]].push_back(v[0]);
        }
        bool b1[numCourses+1],b2[numCourses+1];
        memset(b1,false,sizeof(b1));      
        memset(b2,false,sizeof(b2));      
        for(int i=0;i<numCourses;i++){     
            if(!b1[i])
                if(!cycle(graph,b1,b2,i))   return false;
        }
        return true;
    }
};
