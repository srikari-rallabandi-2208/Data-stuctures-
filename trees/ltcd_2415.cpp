//LeetCode - problem 2415

TreeNode* reverseOddLevels(TreeNode* root) {
	vector<TreeNode*> v;
	v.push_back(root);
	bool isOdd = true;
	while (v.size() != 0) {
		vector<TreeNode*> temp;
		for (TreeNode* n : v) {
			if (n->left) temp.push_back(n->left);
			if (n->right) temp.push_back(n->right);
		}
		if (isOdd) {
			int front = 0, back = temp.size() - 1;
			while (front < back) {
				swap(temp[front]->val, temp[back]->val);
				front++;
				back--;
			}
		}
		v = temp;
		isOdd = !isOdd;
	}
	return root;
}
