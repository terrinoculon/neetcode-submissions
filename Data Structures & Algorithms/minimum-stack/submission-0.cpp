class MinStack {
private:
       std::stack<int> stack, minstack; 

public:
    MinStack() {
    }
    
    void push(int val) {
        stack.push(val);
        if (!minstack.empty()){
            minstack.push(std::min(minstack.top(), val));
        } else {
            minstack.push(val);
        }
    }
    
    void pop() {
        stack.pop();
        minstack.pop();
    }
    
    int top() {
        return stack.top();
    }
    
    int getMin() {
        return minstack.top();
    }
};
