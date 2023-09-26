# Given a string of letters, write a function to see if the word  (case insensitive) is a palindrome (the same word spelled forward and backwards).
# The given string will contain only letters 
# Examples:
# is_palindrome("RaceCar") \\ => True
# is_palindrome("mom")  \\ => True
# is_palindrome("Shoha") \\ => False




def solution(word):
    if word.lower() == word.lower()[::-1]:
        return True
    else:
        return False


def solution(letters):
    return letters.lower() == letters.lower()[::-1]
