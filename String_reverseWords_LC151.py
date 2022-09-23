"""
Reverse the words:
*You need to reduce multiple spaces between two words to a single space in the reversed string.
*Your reversed string should not contain leading or trailing spaces.

input: " the   sky is blue "
output: "blue is sky the"

Step 1) Trim the spaces -> "the sky is blue"
Step 2) Reverse the list-> ['e', 'u', 'l', 'b', ' ', 's', 'i', ' ', 'y', 'k', 's', ' ', 'e', 'h', 't']
Step 3) Reverse the word by detected spaces ->
"""

def reverseWords(inputStr: str) -> str:
    # Trim the spaces
    trimmed_str_list =  trimSpaces(inputStr)
    # Reverse the list
    rev_str_list = reverseList(trimmed_str_list)
    # Reverse the word by detected spaces:
    rev_each_word_list = reverseEachWord(rev_str_list)
    # Transfer the list to a string:
    return ''.join(rev_each_word_list)


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
    for i in range(0, length):
        if inputList[i]== " ":
            if end!=0: # The first word is reversed
                start = end + 1
            end = i
            new_list = reverseList(inputList[start:end])
            list_temp += new_list + [" "]
        if i == length-1: # The last word is reversed
            start = end+1
            end = i+1
            new_list = reverseList(inputList[start:end])
            list_temp += new_list
    #print(list_temp)
    return list_temp



input_string = " the   sky is blue "
print("The input string is:" + input_string)

"""
trimmed_str_list = trimSpaces(input_string)
print("the words with spaces trimmed:" + str(trimmed_str_list))

rev_str_list = reverseList(trimmed_str_list)
print("the reversed words:" + str(rev_str_list))

rev_each_word_list = reverseEachWord(rev_str_list)
print("the reversed words: " + str(rev_each_word_list))
"""

reversedWord1 = reverseWords(input_string)
print("the reversed words:" + reversedWord1)
