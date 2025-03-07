def get_num_words(words):
    num_words = len(words)
    return num_words

def get_char_count(words):
    char_counts = {}
    for word in words:
        for w in word:
            if w.lower() in char_counts:
                char_counts[w.lower()] = char_counts[w.lower()] + 1
            else:
                char_counts.update([(w.lower(), 1)])
    return char_counts

def sort_chars():
    chars = get_char_count()
    my_dict = dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))
    return my_dict