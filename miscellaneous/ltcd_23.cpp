//LeetCode - problem 23

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode *dummy = new ListNode(0), *cur = dummy;
        int n = lists.size(), min = INT_MAX, idx = 0;
        while (true) {
            for (int i = 0; i < n; i++) {
                if (lists[i] && lists[i] -> val < min) {
                    min = lists[i] -> val;
                    idx = i;
                }
            }
            if (min == INT_MAX) {
                break;
            }
            cur -> next = lists[idx];
            cur = cur -> next;
            lists[idx] = lists[idx] -> next;
            min = INT_MAX;
        }
        return dummy -> next;
    }
