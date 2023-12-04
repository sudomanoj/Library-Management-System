import csv
from datetime import date, datetime
class ReturnBook:
    
    def return_book(self):
        try:
            user_id=int(input("Enter member id:"))
            book_id=int(input("Enter id of the book you want to return:"))
        except Exception as E:
            print("Error {E} Enter Number only")
        check_user_borrow=False
        borrowed_date="2023-11-04"
        fine=0
        with open('borrowed_book.csv','r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            for i,row in enumerate(rows):
                if row[0] == str(user_id) and row[1]==str(book_id):
                    borrowed_date=row[2]
                    check_user_borrow=True
                    break
        current_date = date.today()
        saved_date = datetime.strptime(borrowed_date, "%Y-%m-%d").date()
        difference = current_date - saved_date
        days_difference = difference.days
        if check_user_borrow:
            rows.pop(i)
            with open('borrowed_book.csv', 'w', newline='') as updated_file:
                writer = csv.writer(updated_file)
                writer.writerows(rows)
            with open('book_inventory.csv', 'r') as file:
                file_reader = csv.reader(file)
                rows = list(file_reader)
            for row in rows:
                if int(row[0]) == book_id:
                    row[4] = int(row[4]) + 1
                    break
            with open('book_inventory.csv', 'w', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(rows)
            if days_difference>15:
                fine=(days_difference-15)*10
                print(f"Pay fine of Rs {fine}")
            else:
                print("No fine Charged")
        else:
            print("Enter correct member id and book id")