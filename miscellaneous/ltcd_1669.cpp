//LeetCode - problem 1669

    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
       ListNode* t = list1;
        ListNode* pre=list1;
         
        while(a--){
            pre=t;
            t=t->next;
        }
        t=list1;
        while(b--){
            t=t->next;
        }
          t=t->next;
        pre->next=NULL;
        pre->next=list2;
        
        while(list2->next){
            list2=list2->next;
        }
           list2->next=t;
        return list1;
    }
