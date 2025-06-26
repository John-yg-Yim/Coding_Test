class Solution():
    def __init__(self, s):
        self.s = s
    
    def ValidParentheses(self):
        s = self.s
        stack = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            elif s[i] == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif s[i] == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            elif s[i] == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            else:
                raise ValueError(f"유효하지 않은 문자: {s[i]}")
        
        return not stack

def main():
    s1 = "()"
    s2 = "()[]{}"
    s3 = "(]"
    s4 = "([])"

    sol1 = Solution(s1)
    sol2 = Solution(s2)
    sol3 = Solution(s3)
    sol4 = Solution(s4)

    print(sol1.ValidParentheses())
    print(sol2.ValidParentheses())
    print(sol3.ValidParentheses())
    print(sol4.ValidParentheses())

if __name__ == "__main__":
    main()