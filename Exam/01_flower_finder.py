from collections import deque


def check_letters(words, vowel, consonant):
    for word in words.keys():
        words[word] = words[word].replace(vowel, "")
        words[word] = words[word].replace(consonant, "")
    return words


vowels = deque([x for x in input().split()])
consonants = [x for x in input().split()]
found_word = False

words = {
    'rose': 'rose',
    'tulip': 'tulip',
    'lotus': 'lotus',
    'daffodil': 'daffodil'
}

while vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()
    check_letters(words, current_vowel, current_consonant)
    if "" in words.values():
        print(f"Word found: {''.join([word for word in words.keys() if words[word] == ''])}")
        found_word = True
        break
if not found_word:
    print(f"Cannot find any word!" )
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")