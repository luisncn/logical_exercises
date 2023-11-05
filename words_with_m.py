"""
Verify the word that contains the letter m, it is used to analyze the days
with the letter m
"""


class CheckWordsWithM:
    @staticmethod
    def check_word_m(*args):
        words_with_m = []
        for letter in args:
            if "m" in letter.lower():
                words_with_m.append(letter)
        return words_with_m


words = CheckWordsWithM
print(words.check_word_m("Lunes", "Martes", "Miercoles", "Domingo"))
