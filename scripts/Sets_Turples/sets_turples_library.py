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
        return None

    library[title] = {
        "author": author,
        "released": year,
        "inStock": None
    }

    print(f"[add_book]: Добавлена книга '{title}'")


def remove_book(library, title):
    if title not in library:
        print("No such book")
        return None
    library.pop(title)
    print(f"[remove_book]: Удалена книга '{title}'")


library = {"The Silmarillion" : {"author": "John R.R. Tolkien",
                                 "released": 1977,
                                 "inStock": True}}
library_empty = {}

book_list_view(library)
book_list_view(library_empty)

add_book(library, "Name", "Me", 1999)

book_list_view(library)

remove_book(library, "Name")

book_list_view(library)
