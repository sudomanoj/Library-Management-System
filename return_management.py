import csv


class ReturnBook:

    def return_book(self):
        try:
            user_id = int(input("Enter member id:"))
            book_id = int(input("Enter id of the book you want to return:"))
        except ValueError:
            print("Error {E} Enter Number only")
        with open('borrowed_book.csv', 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            row_to_delete = None
            for i, row in enumerate(rows):
                if row[0] == str(user_id) and row[1] == str(book_id):
                    row_to_delete = i
                    break

            if row_to_delete is not None:
                rows.pop(row_to_delete)
            with open('borrowed_book.csv', 'w', newline='') as updated_file:
                writer = csv.writer(updated_file)
                writer.writerows(rows)

                print("success")


