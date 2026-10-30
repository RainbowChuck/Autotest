# ---------------------------Анализ текста-------------------

def text_analysis(text):
    text = text.lower()

    words = text_cleaner(text).split()
    unique_words = set(words)
    longest_word = max(words, key = len)
    let_count = letters_count(text_cleaner(text))

    return longest_word, let_count, words_count(unique_words, text)


def text_cleaner(text):
    cleaned_text = ""
    for ch in text:
        if ch.isalnum():
            cleaned_text += ch
        else:
            cleaned_text += " "
    return cleaned_text


def letters_count(text):
    let_count = 0
    letters = ['а','е','ё','и','о','у','ы','э','ю','я']
    for letter in text:
        if letter in letters:
            let_count += 1
    return let_count


def words_count(unique_words, text):
    word_dict = {}
    for word in unique_words:
        word_dict[word] = text.count(word)
    return word_dict


print(text_analysis("Галаграмма была очень реалистичной"))
print(text_analysis("Субатомный, ? порозориий"))