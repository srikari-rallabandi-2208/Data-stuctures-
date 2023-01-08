//LeetCode - problem 234

    bool isPalindrome(ListNode* head) {
        ListNode *cur = head;//this is the normal cursor
        return judge(head, cur);
    }
    bool judge(ListNode *head, ListNode* &cur) {
        if (!head) return true;
        if (!judge(head->next, cur)) return false;
        if (cur->val != head->val) return false;
        else {cur = cur->next; return true;}
    }
