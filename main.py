from book_management import BookManagement
from user_management import User
from borrow_book import BorrowBook
from return_management import ReturnBook

class LMS(BookManagement,User,BorrowBook,ReturnBook):
    def __init__(self):
        print(f"{'Library Management System':#^100}")
lms=LMS()

def run():
    while True:
        command:str = input('Enter command [add book, view books, add user, borrow, return]:').lower().replace(' ', '')
        try: 
            match command:
                case 'addbook':
                    lms.add_books()      
                case 'viewbooks':
                    lms.show_books() 
                case 'adduser':
                    lms.addUser()
                case 'borrow':
                    lms.borrow()
                case 'return':
                    lms.return_book()
                case 'exit':
                    break
        except Exception as e:
            print(f'An error occured: {e}')

if __name__ == '__main__':       
    run()