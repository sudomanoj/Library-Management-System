from book_management import BookManagement
from user_management import User
class borrowBook(BookManagement):
    def __init__(self):
        print("Borrow Book")
    def borrow(self):
        borrow_book_id=int(input("enter id of book you want to borrow:"))
        check_book=self.checkBook(borrow_book_id)
        check_user_id=int(input("Enter user id to borrow book:"))
        # check_user=pass
borrowB=borrowBook()
borrowB.borrow()