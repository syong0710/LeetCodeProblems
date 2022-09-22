def isPalindrome(string: str) -> bool:
    left, right = 0, len(string) - 1
    while left < right:
        # left/right pointers should be pointing at a alphanumeric character
        # isalnum() method checks if all the characters of string are alphanumeric or not.
        while left < right and not string[left].isalnum():
            left += 1
        while left < right and not string[right].isalnum():
            right -= 1

        if left < right:
            # The lower() method returns a string where all characters are lower case.
            if string[left].lower() != string[right].lower():
                return False
            left += 1
            right -= 1
    return True


#inputString = "A man, a plan, a canal: Panama"
#inputString = "A man, a plan, a canal: Panama    !  #  @"
inputString = "A man, a plan, a canal: Panama    !  #  @1"
print("if palindrome:" + str(isPalindrome(inputString)))