def words_sorting(*args):
    words = dict()
    result = []
    for key in args:
        if not key in words:
            words[key] = sum([int(ord(x)) for x in key])
    if not sum(words.values()) % 2 == 0:
        sorted_words = sorted(words.items(), key=lambda kvpt: kvpt[1], reverse=True)
    else:
        sorted_words = sorted(words.items(), key=lambda kvpt: kvpt[0])
    for el in sorted_words:
        result.append(f"{el[0]} - {el[1]}")
    return "\n".join(result)

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

