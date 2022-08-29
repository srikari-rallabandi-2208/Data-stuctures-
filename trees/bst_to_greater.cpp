void solve(TreeNode* &root,int& mx){
    if(root == NULL) return;
    solve(root->right,mx);
    root->val = root->val + mx;
    mx = root->val;
    solve(root->left,mx);
}

TreeNode* convertBST(TreeNode *root){
    int mx = 0;
    solve(root,mx);
    return root;
}
