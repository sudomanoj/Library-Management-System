from book_management import BookManagement
from user_management import User
from borrow_book import BorrowBook

class LMS(BookManagement,User,BorrowBook):
    def __init__(self):
        print(f"{'Library Management System':#^100}")
lms=LMS()
def run():
    while True:
        command:str = input('Enter command [add book, view books, add user, check user,borrow]:').lower().replace(' ', '')

        match command:
            case 'addbook':
                lms.add_books()      
            case 'viewbooks':
                lms.show_books() 
            case 'adduser':
                lms.addUser()
            case 'borrow':
                lms.borrow()
            case 'exit':
                break

if __name__ == '__main__':       
    run()