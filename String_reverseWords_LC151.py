"""
Reverse the words:
*You need to reduce multiple spaces between two words to a single space in the reversed string.
*Your reversed string should not contain leading or trailing spaces.

input: " the   sky is blue "
output: "blue is sky the"

Step 1) Trim the spaces -> "the sky is blue"
Step 2)
Step 3)
"""


def reverseWords(inputStr: str) ->str:
    return inputStr

# swap cannot be performed in a string, so a list is created.
def trimSpaces(inputStr: str) -> list:
    left = 0
    right = len(inputStr)-1
    # remove the spaces at the head
    while left<=right and inputStr[left] == " ":
        left += 1
    # remove the spaces at the tail
    while left<=right and inputStr[right] == " ":
        right -= 1
    # check multiple spaces between words
    tempStrList = []
    while left<=right:
        if inputStr[left] == " " and tempStrList[-1] == " ":
            left += 1
        else:
            tempStrList.append(inputStr[left])
            left += 1
    return tempStrList


# return the reversed string in list format
def reverseList(inputStrList:list)->list:
    left = 0
    right = len(inputStrList)-1
    while left <= right:
        inputStrList[left], inputStrList[right] = inputStrList[right], inputStrList[left]
        left += 1
        right -=1
    return inputStrList


# reverse each word
def reverseEachWord(inputList:list)->None:
    start = 0
    end = 0
    length = len(inputList)
    list_temp = []
    for i in range(0, length-1):
        if inputList[i]== " " or i==length-1:
            if end!=0:
                start = end-1
            end = i
            new_list = reverseList(inputList[start:end])
            list_temp += new_list
            print(str(start) + str(end))
            print(str(new_list))
            print(str(list_temp))



input_string = " the   sky is blue "
print("The input string is " + input_string)

trimmed_str_list = trimSpaces(input_string)
print("the words with spaces trimmed:" + str(trimmed_str_list))

rev_str_list = reverseList(trimmed_str_list)
print("the reversed words:" + str(rev_str_list))

reverseEachWord(rev_str_list)
print("the reversed words: " + str(rev_str_list))