//LeetCode - problem 232

class Queue {
public:
    void push(int x) {
		while (!nums.empty()) {
			helper.push(nums.top());
			nums.pop();
		}
		nums.push(x);
		while (!helper.empty()) {
			nums.push(helper.top());
			helper.pop();
		}
    }
    void pop(void) {
        nums.pop();
    }
    int peek(void) {
        return nums.top();
    }
    bool empty(void) {
		return nums.empty();
    }
private:
	std::stack<int> helper, nums;
};
