def evalRPN(tokens:list[str]) -> int:
    stack = []
    for item in tokens:
        if item not in {"+", "-", "*", "/"}:
            stack.append(item)
        else:
            first_num, second_num = stack.pop(), stack.pop()
            stack.append(
                int(eval(f'{second_num} {item} {first_num}'))
            )
    return int(stack.pop())


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
#tokens = ["2","1","+","3","*"]
#tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

print("result = " + str(evalRPN(tokens)))

