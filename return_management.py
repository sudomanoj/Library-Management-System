import csv
class ReturnBook:
    
    def return_book(self):
        try:
            user_id=int(input("Enter member id:"))
            book_id=int(input("Enter id of the book you want to return:"))
        except Exception as E:
            print("Error {E} Enter Number only")
        with open('borrowed_book.csv','r') as file:
            reader = csv.reader(file)
            check_user_borrow = any((True for row in reader if row[0] == str(user_id) and row[1]==str(book_id)))
        if check_user_borrow:
            print(row)
            # with open('book_inventory.csv', 'r') as file:
            #     file_reader = csv.reader(file)
            #     rows = list(file_reader)
            # for row in rows:
            #     if int(row[0]) == book_id:
            #         row[4] = int(row[4]) + 1
            #         break
            # with open('book_inventory.csv', 'w', newline='') as file:
            #     csv_writer = csv.writer(file)
            #     csv_writer.writerows(rows)
        else:
            print("Enter correct member id and book id")