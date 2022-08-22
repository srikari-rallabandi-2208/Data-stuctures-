//LeetCode - problem 86

    ListNode* partition(ListNode* head, int x) {
        if(head==NULL || head->next==NULL) return head;
        ListNode* ptr = head;
        ListNode* prev = NULL;
        ListNode* cptr = NULL;
        ListNode* prevcptr = NULL;
        int flag=0;
        while(ptr!=NULL)
        {
            if(ptr->val<x && cptr!=NULL)
            {
                    prev->next = ptr->next;
                    ptr->next = cptr;
                    if(prevcptr!=NULL) prevcptr->next = ptr;
                    if(cptr==head)
                    {
                        head = ptr;
                    }
                    cptr = ptr->next;
                    prevcptr = ptr;
                    prev = cptr;
                    ptr = cptr->next;
            }
            else if(ptr->val>=x && flag==0) 
            {
                flag=1;
                prevcptr = prev;
                cptr = ptr;
                prev = ptr;
                ptr = ptr->next;
            }
            else{
                
                prev = ptr;
                ptr = ptr->next;
            }
        }
     return head;   
}
