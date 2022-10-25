//LeetCode - problem 199

    void dfs(TreeNode* root, int level, vector<int>&res){
        if(!root)
            return;
        if(res.size()==level) res.push_back(root->val);
        dfs(root->right,level+1,res);
        dfs(root->left,level+1,res);
    }

    vector<int> rightSideView(TreeNode* root){
        vector<int> res;
        dfs(root,0,res);
        return res;
    }
