def individual_book_data(book):
    return {
        "id": str(book["_id"]),
        "title": book["title"],
        "author": book["author"],
        "Description": book["description"],
    }


def all_book_data(books):
    return [individual_book_data(book) for book in books]
