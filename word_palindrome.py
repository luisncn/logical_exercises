"""
Reverses the text of a given string and checks if the word is palindrome.
"""


class CheckWordPalindrome:
    @staticmethod
    def reverse_word(word):
        inverted_word = ""
        for x in word:
            inverted_word = x + inverted_word
        if word.upper() == inverted_word.upper():
            print(f"La palabra {word} es Palindrome")
        else:
            print(f"La palabra {word} no es Palindrome")


check = CheckWordPalindrome()
check.reverse_word("oso")
