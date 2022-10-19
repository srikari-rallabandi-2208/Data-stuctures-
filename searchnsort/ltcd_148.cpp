//LeetCode - problem 148

  ListNode* sortList(ListNode* head) {
    if (!head || !head->next) return head;

    ListNode* mid = findMid(head);
    ListNode* head2 = mid->next;
    mid->next = NULL;

    ListNode* l = sortList(head);
    ListNode* r = sortList(head2);

    return merge(l, r);
  }

  ListNode* merge(ListNode* l, ListNode* r) {
    ListNode* dummy = new ListNode(-1);
    ListNode* cur = dummy;

    while (l && r) {
      if (l->val < r->val) {
        cur->next = l;
        l = l->next;
      } else {
        cur->next = r;
        r = r->next;
      }
      cur = cur->next;
    }

    if (l) cur->next = l;
    if (r) cur->next = r;

    return dummy->next;
  }

  ListNode* findMid(ListNode* head) {
    ListNode* cur = head;
    ListNode* fast = head;
    ListNode* slow = head;

    while (fast && fast->next && fast->next->next) {
      fast = fast->next->next;
      slow = slow->next;
    }
    return slow;
  }
