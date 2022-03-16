//leetcode problem - 1302 : deepest leaves sum


class Solution {
public:
    int depth=0, ans=0;
    void solve(TreeNode* root, int k){
        if(!root) return;
        if(root->left==NULL and root->right==NULL)
            depth=max(depth,k);
        solve(root->left,k+1);
        solve(root->right, k+1);
    }
    void findans(TreeNode* root, int k){
        if(!root) return;
        if(k==depth)
            ans+=root->val;
        findans(root->left, k+1);
        findans(root->right, k+1);
    }
    int deepestLeavesSum(TreeNode* root) {
        solve(root,1);
        findans(root,1);
        return ans;
    }
};
