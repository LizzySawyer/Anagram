# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word1, word2):
    # [assignment] Add your code here
    word1 = input(str("first word: "))
    word2 = input(str("second word: "))
    if sorted(word1) == sorted(word2):
        return True 
    if sorted(word1) != sorted(word2):
        return False

print(find_anagrams('first word', 'second word'))













