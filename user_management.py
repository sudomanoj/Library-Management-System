import csv


class User:
    _user_id = 0

    def __init__(self):
        print("User instance")

    @classmethod
    def getUser_id(cls):
        with open('user_id.log', 'r') as file:
            for f in file:
                cls._user_id = int(f)
        cls._user_id += 1
        with open('user_id.log', 'w') as file:
            file.write(str(cls._user_id))
        return cls._user_id

    def addUser(self):
        full_name = input("Enter your full name:")
        try:
            contact_no = int(input("Enter your contact number:"))
        except Exception as E:
            print("Error={E}! Enter number only")
            return
        duplicate_number = False
        with open('user.csv', 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for r in csvreader:
                if int(r[2]) == contact_no:
                    duplicate_number = True
                    break
        if duplicate_number:
            print("Duplicate Number Found!")
        else:
            user_id = self.getUser_id()
            with open('user.csv', 'a', newline='\n') as file:
                writer = csv.writer(file)
                writer.writerow([user_id, full_name, contact_no])
            print("User sucessfully Created")

    def checkUser(self, user_id):
        with open('user.csv', 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for r in csvreader:
                if int(r[0]) == user_id:
                    return True
                    break
            return False
