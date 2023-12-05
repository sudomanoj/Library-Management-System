from book_management import BookManagement
from user_management import User
from borrow_book import BorrowBook
from return_management import ReturnBook

class LMS(BookManagement,User,BorrowBook,ReturnBook):
    def __init__(self):
        print(f"{'Library Management System':#^100}")
    def help_msg(self):
        print(f"{'Possible command':#^100}")
        print("addbook->Add new book in inventory")
        print("viewbooks->View avaliable books in Library")
        print("adduser->register user in Library")
        print("borrow->Borrow book from Library")
        print("return->Return book to Library")
        print("help->All LMS commands")
        print("exit->Exit LMS system")
        print(f"{'End of command':#^100}")
lms=LMS()

def run():
    while True:
        command:str = input('Enter command [addbook, viewbooks, adduser, borrow, return,help,exit]:').lower().replace(' ', '')
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
                case 'help':
                    lms.help_msg()
                case 'exit':
                    break
        except Exception as e:
            print(f'An error occured: {e}')

if __name__ == '__main__':       
    run()