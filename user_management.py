class User:
    _user_id=0
    def __init__(self):
        print("User instance")
    @classmethod
    def getUser_id(cls):
        with open('user_id.log','r') as file:
            for f in file:
                cls._user_id=int(f)
        cls._user_id+=1
        with open('user_id.log','w') as file:
            file.write(str(cls._user_id))
        return cls._user_id
    def addUser(self):
        full_name=input("Enter your full name:")
        contact_no=int(input("Enter your contact number:"))
        with open('user.csv','r') as file:
            for f in file:
                pass
print(User.getUser_id())