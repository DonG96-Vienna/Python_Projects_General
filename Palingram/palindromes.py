"""Palindrome finden"""

from load_dictionary import load

word_list = load('dictionary.txt')
palin_list = []

# Wort muss vorwärts = rückwarts sein
for word in word_list:
    if len(word) > 1 and word[::-1] == word:
        palin_list.append(word)

print(f"Number of palindroms is {len(palin_list)}.")
print(f"The words are: \n")
print(*palin_list, sep='\n')