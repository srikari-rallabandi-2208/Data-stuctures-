//LeetCode - problem 83

    ListNode* deleteDuplicates(ListNode* head) {
        if(head==NULL || head->next==NULL)
            return head;
        head->next=deleteDuplicates(head->next); 
        if(head->val==head->next->val) 
            return head->next;
        else
            return head;
    }
