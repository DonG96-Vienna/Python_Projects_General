'''

Palingramme finden.
2 Wörter die vorwärts und rückwärts gleich aussehen

'''

from load_dictionary import load

word_list = load('dictionary.txt')

def find_palingrams():
    """Wortpaare aus dictionary finden"""

    pali_list = []

    # Set, da es optimierter ist verglichen mit List
    words = set(word_list)
    for word in words:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in words:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in words:
                    pali_list.append((rev_word[:end-i], word))

    return  pali_list

palingrams = find_palingrams()

palingrams_sorted = sorted(palingrams)

print(f"Number of palingrams = {len(palingrams_sorted)}.")
for first, second in palingrams_sorted:
    print(f"{first} {second}")