def book_list_view(library):
    if library:
        print(f"[book_list_view]: ")
        for title in library:
            print(title)
    else:
        print("No books")


def add_book(library):
    title  = input("Введите название книги: ")
    if title in library:
        print(f"[add_book]: Книга с названием '{title}' Уже существует")
        return
    author = input("Введите Автора: ")
    year = input("Введите год: ")

    library[title] = {
        "author": author,
        "released": year,
        "in_stock": None
    }

    print(f"[add_book]: Добавлена книга '{title}'")


def remove_book(library):
    print("[remove_book]: ", library.keys())
    title = input("Какую книгу удалить? ")
    if title not in library:
        print("Нет такой книги")
        return
    library.pop(title)

    print(f"[remove_book]: Удалена книга '{title}'")


def issue_book(library, ):
    print("[issue_book]: ", library.keys())
    title = input("Какую книгу выдать? ")
    if title in library and library[title]["in_stock"] is True:
        library[title]["in_stock"] = False
        print(f"The book {title} successfully issued")
    elif title in library and library[title]["in_stock"] is None:
        print("This book is unavailable to burry, please try again later")
    elif title in library and library[title]["in_stock"] is False:
        print("This book is already issued")
    else:
        print("Нет такой книги")


def return_book(library):
    print("[return_book]: ", library.keys())
    title = input("Какую книгу вернуть? ")
    if title in library:
        library[title]["in_stock"] = True
        print(f"The book {title} successfully returned")
    else:
        print("Нет такой книги")


def find_book(library):
    print("[find_book]: ", library.keys())
    title = input("Какую книгу найти? ")
    if title in library:
        print(f"[find_book]: Book found: {title}"
              f", written by {library[title]['author']}"
              f" in {library[title]['released']},")
    else:
        print(f"The book '{title}' is not found")
        return

    if library[title]['in_stock'] is True:
        print("Книга доступна")
    elif library[title]['in_stock'] is False:
        print("Книга выдана")
    elif library[title]['in_stock'] is None:
        print("Книга в библиотеке, но её статус не определен")


def program_end(library):
    print(f"Programmed in library {library} ended its work")
    return False


def user_interface(library):
    # is_working = True
    menu_options = {"1" : ("Find Book", find_book),
                    "2" : ("Return Book", return_book),
                    "3": ("Issue Book", issue_book),
                    "4" : ("Remove Book", remove_book),
                    "5" : ("Add Book", add_book),
                    "6" : ("Show Books", book_list_view),
                    "7" : ("Quit", program_end)}
    while True:
        choice = input("""1 : "Find Book"
2 : "Return Book"
3 : "Issue Book",
4 : "Remove Book"
5 : "Add Book"
6 : "Show Books"
7 : "Quit"
Please select an option: """)
        if choice in menu_options:
            if menu_options[choice][1](library) is False:
                break


library = {"The Silmarillion" : {"author": "John R.R. Tolkien",
                                 "released": 1977,
                                 "in_stock": True}}

user_interface(library)

# library_empty = {}
#
# book_list_view(library)
# book_list_view(library_empty)
#
# add_book(library, "Name", "Me", 1999)
#
# book_list_view(library)
#
# remove_book(library, "Name")
#
# book_list_view(library)
#
# issue_book(library, "The Silmarillion")
# issue_book(library, "The Silmarillion")
# issue_book(library, "Name")
# return_book(library, "The Silmarillion")
#
# find_book(library, "The Silmarillion")
# find_book(library, "Name")
