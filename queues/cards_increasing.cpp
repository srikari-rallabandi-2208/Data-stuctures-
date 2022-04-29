//LeetCode - problem 950

vector<int> deckRevealedIncreasing(vector<int>& v) {
        sort(v.begin(),v.end());
        deque<int> dq;
        while(!v.empty()) {
            int el = v[v.size()-1];
            v.pop_back();
            if(!dq.empty()) {
                int x = dq.back();
                dq.pop_back();
                dq.push_front(x);
            }
            dq.push_front(el);
        }
        return vector<int>(dq.begin(),dq.end());
    }
