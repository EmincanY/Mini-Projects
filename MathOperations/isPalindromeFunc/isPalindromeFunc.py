# Palindrome Function.
# A palindrome word reads same backward as forward. Such as "madam" or "racecar"

def isPalindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(isPalindrome("madam"))
