import csv
from datetime import datetime, timedelta
from typing import Union


class BorrowBook:
    ROW_NAME = ['userID', 'bookID', 'borrowDateTime', 'dayCount']

    def borrow(self):
        while True:
            member_id = int(input("Enter the member ID: "))
            if self.check_member_exists(member_id):
                break
            else:
                print("Member doesn't exists, please reenter the member id")

        while not self.borrow_exceed(member_id):
            book_id = int(input("Enter the book ID: "))
            if self.check_book_exists(book_id) and self.check_book_quantity(book_id):
                borrowed_date_timestamp = datetime.now()
                day_count = 0
                data = [member_id, book_id, borrowed_date_timestamp, day_count]

                with open('borrowed_book.csv', 'a') as borrowed_file:
                    borrowed_writer = csv.writer(borrowed_file)
                    if borrowed_file.tell() == 0:
                        borrowed_writer.writerow(self.ROW_NAME)
                    borrowed_writer.writerow(data)

                self.decrease_quantity(book_id)
                print("Book borrowed successfully.")
                borrow_another = input("Do you want to borrow another book? (yes/no): ").lower()
                if borrow_another != 'yes':
                    break
            if not self.check_book_exists(book_id):
                print("Book doesn't exist invalid book id")
            if not self.check_book_quantity(book_id):
                print("Book out of stock")

        else:
            print("You can't borrow more than 3 books")

    def borrow_exceed(self, member_id: int) -> bool:
        with open("borrowed_book.csv", 'r') as borrow_book:
            borrow_book_reader = csv.reader(borrow_book)
            count = 0
            for row in borrow_book_reader:
                if row and row[0] == str(member_id):
                    count += 1
                    if count > 3:
                        return True
                        break

    def decrease_quantity(self, book_id: int) -> None:
        with open('book_inventory.csv', 'r') as file:
            file_reader = csv.reader(file)
            rows = list(file_reader)
        for row in rows:
            if int(row[0]) == book_id:
                row[4] = int(row[4]) - 1
                break

        with open('book_inventory.csv', 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(rows)

        print("updated")

    @staticmethod
    def check_member_exists(member_id: int) -> bool:
        """Checks the member exists or not  if not returns False"""
        with open("user.csv", "r") as user:
            user_reader = csv.reader(user)
            member = any((True for row in user_reader if row[0] == str(member_id)))
            return member

    @staticmethod
    def check_book_exists(book_id: int) -> Union[dict, None]:
        with open('book_inventory.csv', 'r') as file:
            reader = csv.reader(file)
            book = any((True for row in reader if row[0] == str(book_id)))
            return book

    @staticmethod
    def check_book_quantity(book_id: int) -> int:
        with open("book_inventory.csv", 'r') as file:
            reader = csv.reader(file)
            quantity = any((True for row in reader if int(row[4]) > 0))
            return quantity

