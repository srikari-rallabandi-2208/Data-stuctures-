//LeetCode - problem 1206

class Skiplist {
private:
    const int kMaxHeight = 8;
    
    struct Node {
        int val;
        int height;
        Node** next;
        
        Node(int v, int h) {
            val = v;
            height = h;
            next = new Node*[h];
            while (--h >= 0) next[h] = nullptr;
        }
        
        ~Node() {
           delete [] next;
        }
    };
    
    int getRandomHeight() {
        int h = 1;
        while (h < kMaxHeight && rand() % 4 == 1) ++h;
        
        return h;
    }
    
    
    Node* findGreaterOrEqual(int target, Node** prev) {
        Node* it = head;
        int level = kMaxHeight-1;
        while (true) {
            Node* next = it->next[level];
            if (next && next->val < target) {
                it = next;
            } else {
                if (prev)  prev[level] = it;
                
                if (level == 0) {
                    return next;
                } else {
                    --level;
                }
            }
        }
    }
    
    
    Node* head;
public:
    Skiplist() {
        head = new Node(0, kMaxHeight);
    }
    
    bool search(int target) {
        Node* node = findGreaterOrEqual(target, nullptr);
        return node != nullptr && node->val == target;
    }
    
    void add(int num) {
        Node* prev[kMaxHeight];
        findGreaterOrEqual(num, prev);
        
        Node* node = new Node(num, getRandomHeight());  
        for (int i = 0; i < node->height; ++i) {
            node->next[i] = prev[i]->next[i];
            prev[i]->next[i] = node;
        }
    }
    
    bool erase(int num) {
        Node* prev[kMaxHeight];
        Node* to_del = findGreaterOrEqual(num, prev);
        if (to_del == nullptr || to_del->val != num) {
            return false;
        }
        
        for (int i = 0; i < to_del->height; ++i) {
            prev[i]->next[i] = to_del->next[i];
        }
        
        delete to_del;
        return true;
    }
};
