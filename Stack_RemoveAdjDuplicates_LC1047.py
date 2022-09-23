def removeDuplicates(inputStr:str) -> str:
    result = list()
    for item in inputStr:
        if result and item == result[-1]:
            result.pop()
        else:
            result.append(item)
        #print(str(result))
    return "".join(result)

input_string = 'rrrr12aab33cdd4'
print("the string duplicates removed:" + str(removeDuplicates(input_string)))



