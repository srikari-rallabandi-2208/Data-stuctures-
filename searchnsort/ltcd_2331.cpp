//LeetCode - problem 2331

    bool evaluateTree(TreeNode* root) {
        if (root->left==NULL) return root->val;
        if (root->val==2) return evaluateTree(root->left)||evaluateTree(root->right);
        return evaluateTree(root->left)&&evaluateTree(root->right);
    }
