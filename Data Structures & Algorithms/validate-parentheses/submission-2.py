class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Map every closing bracket to its corresponding opening bracket
        closeToOpen = { ")" : "(", "]" : "[", "}": "{" }

        for c in s:
            # If it's a closing bracket
            if c in closeToOpen:
                # Check if stack is not empty and top of stack matches the opening
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop() # Valid pair found, remove it from stack
                else:
                    return False # Mismatch or unexpected closing bracket
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(c)

        # If the stack is empty as the end, all brackets were matched
        return not stack