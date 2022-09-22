def ifValidAnagram(inputStr1:str, inputStr2:str) -> bool:
    record = [0]*26
    for ind in range(len(inputStr1)):
        record[ord(inputStr1[ind])-ord("a")] += 1
    print(record)
    for ind in range(len(inputStr2)):
        record[ord(inputStr2[ind])-ord("a")] -= 1
    print(record)
    for ind in range(26):
        if record[ind]!=0:
            return False
    return True

str1 = "aeeanazz"
str2 = "zeaenaaz"
#str2 = "reaenaaz"
print("if the strings are anagram: " + str(ifValidAnagram(str1,str2)))

#print(ord("a"))
