import os
import re
import string


class Text:
    def __init__(self, file_name):
        if not os.path.exists(file_name):
            raise FileNotFoundError("File not found")
        self.file = file_name

    def count_characters(self):
        with open(self.file, 'r', encoding='utf-8') as file:
            s = string.whitespace
            return sum(len(lines) - lines.count(char) for char in s for lines in file)

    def count_words(self):
        with open(self.file, encoding="utf-8") as file:
            return sum(
                len(re.findall(r"[a-zA-Zа-яА-ЯёЁіІїЇ0-9]+[,.'-]*[a-zA-Zа-яА-ЯёЁіІєЄїЇ0-9]+", lines)) for lines in file)

    def count_sentenses(self):
        with open(self.file, encoding="utf-8") as file:
            return sum(len(re.findall(r"[A-ZА-ЯЁІЇ][^\.!?]*[\.!?]+", lines)) for lines in file)


test = Text('text_for_test.txt')

print(test.count_characters())
print(test.count_words())
print(test.count_sentenses())