def book_list_view(library):
    if library:
        print(f"[book_list_view]: ")
        for title in library:
            print(title)
    else:
        print("No books")


def add_book(library, title, author, year):
    if title in library:
        print(f"[add_book]: Книга с названием '{title}' Уже существует")
        return

    library[title] = {
        "author": author,
        "released": year,
        "in_stock": None
    }

    print(f"[add_book]: Добавлена книга '{title}'")


def remove_book(library, title):
    if title not in library:
        print("No such book")
        return
    library.pop(title)

    print(f"[remove_book]: Удалена книга '{title}'")


def issue_book(library, title):
    if title in library and library[title]["in_stock"] is True:
        library[title]["in_stock"] = False
        print(f"The book {title} successfully issued")
    elif title in library and library[title]["in_stock"] is None:
        print("This book is unavailable to burry, please try again later")
    elif title in library and library[title]["in_stock"] is False:
        print("This book is already issued")
    else:
        print("No such book")


def return_book(library, title):
    if title in library:
        library[title]["in_stock"] = True
    else:
        print("No such book")


def find_book(library, title):
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


library = {"The Silmarillion" : {"author": "John R.R. Tolkien",
                                 "released": 1977,
                                 "in_stock": True}}
library_empty = {}

book_list_view(library)
book_list_view(library_empty)

add_book(library, "Name", "Me", 1999)

book_list_view(library)

remove_book(library, "Name")

book_list_view(library)

issue_book(library, "The Silmarillion")
issue_book(library, "The Silmarillion")
issue_book(library, "Name")
return_book(library, "The Silmarillion")

find_book(library, "The Silmarillion")
find_book(library, "Name")
