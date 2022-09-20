class Solution {
public:
    bool isValid(string s) {
    stack<char> st;
    bool balanced=true;
    for(auto c: s){
        if (c == '}' || c == ']' || c == ')'){
            if(!st.empty()) {
                char adj = st.top();
                st.pop();
                if ((c == '}' && adj != '{') || (c == ']' && adj != '[') || (c == ')' && adj != '(')) {
                    return false;
                }
            }else{
                return false;
            }
        }else{
            st.push(c);
        }
    }
    if(balanced && st.empty()) return true;
    else return false;
    return 1; 
    }
};