//LeetCode - problem 817

    int numComponents(ListNode* head, vector<int>& G) {
        unordered_set<int> s(G.begin(), G.end());
        bool found = false;
        int n = 0;
        while (head != nullptr) {
            if (s.count(head->val)) {
                if (!found) {
                    found = true;  
                    n++;
                } 
            } else {
                found = false;
            }
            head = head->next;
        }
        return n;
    }
