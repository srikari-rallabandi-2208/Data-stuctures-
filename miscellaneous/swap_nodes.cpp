//leetcode problem 24 - swapping nodes in pairs

struct ListNode{
	int value;
	ListNode *next;
	ListNode(): value(0), next(nullptr){}
	ListNode(int x):value(x), next(nullptr){}
	ListNode(int x, ListNode *next):value(x), next(next){}
};

ListNode* swapPairs(ListNode* head){
	if(head == NULL || head -> next == NULL)
		return head;
	ListNode *node = head;
	ListNode *curr = head;

	node = curr -> next;
	curr -> next = swapPairs(head -> next -> next);
	node -> next = curr;
	head = node;
	return head;
}
