//LeetCode - problem 2385

TreeNode* find(TreeNode* root,int target){
        if(!root)return NULL;
        if(root->val==target)return root;
        TreeNode* r =find(root->right,target);
        TreeNode* l =find(root->left,target);
        if(!l){
            return r;
        }
        else
            return l;
    }
    int amountOfTime(TreeNode* root, int start) {
        map<TreeNode*,TreeNode*>mp;
        queue<TreeNode*>q;
        q.push(root);
        while(!q.empty()){
            int size=q.size();
            for(int i=0;i<size;i++){
                TreeNode* x=q.front();
                q.pop();
                if(x->left){
                    q.push(x->left);
                    mp[x->left]=x;
                }
                if(x->right){
                    q.push(x->right);
                    mp[x->right]=x;
                }
            }
        }
        
        map<TreeNode*,int >vis;
        int res=0;
        TreeNode* t=find(root,start);
        q.push(t);
        vis[t]=1;
        while(!q.empty()){
            int size=q.size();
            int flg=0;
            for(int i=0;i<size;i++){
                TreeNode* x=q.front();
                q.pop();
                
                if((x->left) && !vis[x->left]){
                    q.push(x->left);
                    vis[x->left]=1;
                    flg=1;
                }
                if((x->right) && !vis[x->right] ){
                    q.push(x->right);
                    vis[x->right]=1;
                    flg=1;
                }
                if(mp[x] && !vis[mp[x]]){
                    flg=1;
                    vis[mp[x]]=1;
                    q.push(mp[x]);
                }
            }
            if(flg)res++;
        }
        return res;
    }
