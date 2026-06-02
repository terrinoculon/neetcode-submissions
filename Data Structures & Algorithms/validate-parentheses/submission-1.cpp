class Solution {
public:
    bool isValid(string s) {
        std::stack<char> stack;
        std::unordered_map<char, char> mmap = {{'}','{'},{']','['},{')','('}};
        for (auto c:s){
            if (mmap.count(c)){
                if (!stack.empty() && (stack.top() == mmap[c])){
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                stack.push(c);
            }
        }
        return stack.empty();
    }
};
