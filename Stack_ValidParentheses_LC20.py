
def isValidParentheses(inputString:str) -> bool:
    stack = []
    for item in inputString:
        if item == '(':
            stack.append(')')
        elif item == '[':
            stack.append(']')
        elif item == '{':
            stack.append('}')
        elif not stack or stack[-1] != item:
            return False
        else:
            stack.pop()
    if not stack:
        return True
    else:
        return False


#input_str = '[]()[()]'
input_str = '[]()[()]'
print("if the parentheses are valid: " + str(isValidParentheses(input_str)))





