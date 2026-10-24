# -------------------Обратный отсчет-----------------------
# def ca_boom(a):
#     while a >= 0:
#         print(a)
#         a-=1
#     return print("Ca-Boom")
# ca_boom(5)
from enum import unique

# ---------------------------Пароль--------------------------

# password = ""
# true_password = "0000"
# while password != true_password:
#     password = input("please input your password: ")
# print("Password is: true")

# ---------------------------Анализ текста-------------------

# def text_analysis(text):
#     text = text.lower()
#     cleaned_text = ""
#     for ch in text:
#         if ch.isalnum():
#             cleaned_text += ch
#         else: cleaned_text += " "
#     print(cleaned_text)
#     words = cleaned_text.split()
#     unique_words = set(words)
#     longest_word = max(words,key=len)
#     let_count = letters_count(cleaned_text)
#     word_dict = {}
#     for word in unique_words:
#         word_dict[word] = words_count(words,word)
#     # word_dict = dict.fromkeys(unique_words)
#     # for word in unique_words:
#     #     word_dict[word] = words_count(text, word)
#     return longest_word, let_count, word_dict
#
# def letters_count(text):
#     let_count = 0
#     letters = ['а','е','ё','и','о','у','ы','э','ю','я']
#     for letter in text:
#         if letter in letters:
#             let_count += 1
#     return let_count
#
# def words_count(text, word):
#     return text.count(word)
#
# print(text_analysis("Галаграмма была очень реалистичной"))
#
# print(text_analysis("Субатомный,  ? порозориий"))

# --------------------------Применение условий---------------

def sum_one_to_hundred():
    sum = 0
    for i in range(101):
        if i%2==0:
            sum+=i
    return sum
print(sum_one_to_hundred())

odds = [x**2 for x in range(11) if x%2!=0]
print(odds)

def strange_function():
    counter = 0
    try:
        while int(input("Введите число, отрицательное, чтобы остановиться")) > 0:
            counter += 1
    finally:
        pass
    return counter

print(strange_function())
