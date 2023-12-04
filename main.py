import book_management
import user_management
import borrow_book

def run():
    while True:
        command:str = input('Enter command [add book, view books, check book, add user, check user]').lower().replace(' ', '')

        match command:
            case 'addbook':
                book_management.BookManagement.add_books()
            
            case 'viewbooks':
                book_management.BookManagement.show_books()
                
            
            case 'checkbook':
                book_management.BookManagement.checkBook()
            
            case 'adduser':
                user_management.User.addUser()
            
            case 'checkuser':
                user_management.User.checkUser()
                
            case 'exit':
                break 

if __name__ == '__main__':       
    run()