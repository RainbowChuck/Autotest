# ---------------------------Анализ текста-------------------
def text_analysis(text):
    if isinstance(text, str):
        text = text.lower()
        cleaned_text = text_cleaner(text)
        words = cleaned_text.split()

        if not words:
            return None, 0, {}

        unique_words = set(words)
        longest_word = max(words, key=len)
        let_count = letters_count(cleaned_text)

        return longest_word, let_count, words_count(unique_words, words)

    else:
        print("для анализа необходим исключительно текст")


def text_cleaner(text):
    punctuation = '.,!?;:()[]{}"\'«»—–…„“”№'
    cleaned_text = []

    for word in text.split():
        word = word.strip(punctuation)
        if word:
            cleaned_text.append(word)

    return ' '.join(cleaned_text)


def letters_count(text):
    let_count = 0
    letters = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']

    for letter in text:
        if letter in letters:
            let_count += 1

    return let_count


def words_count(unique_words, words):
    word_dict = {}

    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1

    return word_dict


print(text_analysis("Галаграмма была очень реалистичной"))
print(text_analysis("Субатомный, ? порозориий, субатомный"))
print(text_analysis(134))
print(text_analysis(" "))



