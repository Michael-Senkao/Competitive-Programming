class Solution {
public:
    string decodeString(string s) {
        std::stack<char> stack;
        int n = s.size();

        for (char ch : s) {
            if (ch == ']') {
                std::string curr_word = "";
                std::string k_str = "";

                // Collect the current word
                while (isalpha(stack.top())) {
                    curr_word = stack.top() + curr_word;
                    stack.pop();
                }

                // Remove the '['
                if (!stack.empty() && stack.top() == '[') {
                    stack.pop();
                }

                // Collect the number k
                while (!stack.empty() && isdigit(stack.top())) {
                    k_str = stack.top() + k_str;
                    stack.pop();
                }

                // Convert k_str to integer k
                int k = std::stoi(k_str);

                // Repeat the curr_word k times and push back to stack
                std::string repeated_word = "";
                for (int i = 0; i < k; i++) {
                    repeated_word += curr_word;
                }

                // Push the repeated word back to the stack
                for (char c : repeated_word) {
                    stack.push(c);
                }
            } else {
                stack.push(ch);
            }
        }

        // Construct the final decoded string
        std::string result = "";
        while (!stack.empty()) {
            result = stack.top() + result;
            stack.pop();
        }

        return result;

    }
};