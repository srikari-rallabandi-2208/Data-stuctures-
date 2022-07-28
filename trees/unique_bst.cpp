//LeetCode problem - 95

vector<TreeNode *> generateTree(int from, int to)
{
    vector<TreeNode *> ret;
    if(to - from < 0) ret.push_back(0);
    if(to - from == 0) ret.push_back(new TreeNode(from));
    if(to - from > 0)
    {
        for(int i=from; i<=to; i++)
        {
            vector<TreeNode *> l = generateTree(from, i-1);
            vector<TreeNode *> r = generateTree(i+1, to);

            for(int j=0; j<l.size(); j++)
            {
                for(int k=0; k<r.size(); k++)
                {
                    TreeNode * h = new TreeNode (i);
                    h->left = l[j];
                    h->right = r[k];
                    ret.push_back(h);
                }
            }
        }
    }
    return ret;
}

vector<TreeNode *> generateTrees(int n) {
    return generateTree(1, n);
}
