import csv
from datetime import datetime
class Idgenerator:
    id = 0
    @classmethod
    def get_next_id(cls):
        with open('book_id.log', 'r') as file:
            for f in file:
                cls.id = int(f)
        cls.id += 1
        with open('book_id.log', 'w') as file:
                  file.write(str(cls.id))
        return cls.id

class BookManagement:  
    
    def add_books(self):
        try:
            book_id = Idgenerator.get_next_id()
            book_name = input('Book Name: ')
            author_name = input('Author Name: ')
            genre = input('Book Genre: ')
            try:
                quantity = int(input('Quantity: '))
            except:
                print('Quantity must be an Integer value!!')
                return
            
            try:
                with open('book_inventory.csv', 'r', newline='') as file: 
                    reader = csv.reader(file)
                    global data
                    data = list(reader)
                    if data:
                        found = False
                        for book in data:
                            if book[1] == book_name:
                                book[4] = int(book[4]) +  int(quantity)
                                found = True
                                break   
            except Exception as e:
                print(e)
            if not data:
                try:
                    with open('book_inventory.csv', 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([book_id, book_name, author_name,  genre, quantity])
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)
    
    def show_books(self):
        try:
            with open('book_inventory.csv', 'r+', newline='') as file:
                reader = csv.reader(file)
                books = list(reader)
                if books:
                    for book in books:
                        print(f"""
                        Book Id: {book[0]}
                        Book Name: {book[1]}
                        Author Name: {book[2]}
                        Genre: {book[3]}
                        Quantity: {book[4]}
                        **********************************************
                        """)
        except Exception as e:
            print(e)

b = BookManagement()
b.add_books()