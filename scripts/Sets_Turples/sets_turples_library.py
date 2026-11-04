library = {'name': "The Silmarillion", 'data': {"author": "John R.R. Tolkien", "realised": 1977, "inStock": True}}
library_empty = {}
def book_list_view(library):
    if library:
        print("[book_list_view]: ", library["name"])
    else:
        print("No books")

book_list_view(library)
book_list_view(library_empty)