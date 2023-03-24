def solution(phone_book):
    phone_book = sorted(phone_book)
    for book1, book2 in zip(phone_book, phone_book[1:]):
        if book2.startswith(book1):
            return False
    return True