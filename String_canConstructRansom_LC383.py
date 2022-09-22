def conConstruct(ransomNote:str, magazine:str) -> bool:
    hashTable = [0]*26
    for j in range(len(magazine)):
        hashTable[ord(magazine[j]) - ord("a")] += 1

    for i in range(len(ransomNote)):
        if hashTable[ord(ransomNote[i]) - ord("a")] == 0:
            return False
        else:
            hashTable[ord(ransomNote[i]) - ord("a")] -= 1
    return True


ransom1 = "aabc"
magazine1 = "aba"
print("if the ransom can be written by the magazine: " + str(conConstruct(ransom1, magazine1)))
