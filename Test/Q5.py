# Create a Login System: (4 Marks)
# • Private variable __password = 'python@123'
# • Private variable __attempts = 3
# • Method login(password):
# fi Wrong password: attempts -= 1, show remaining
# fi If attempts == 0: raise AccountLockedError


class AccountLockedError(Exception):
    pass


class LoginSystem:
    def __init__(self):
        self.__password = "python@123"
        self.__attempts = 3

    def login(self, password):
        try:
            if self.__attempts == 0:
                raise AccountLockedError("Account Locked!")

            if password == self.__password:
                print("Login Successful")
            else:
                self.__attempts -= 1
                print("Wrong Password!")
                print("Remaining Attempts:", self.__attempts)

                if self.__attempts == 0:
                    raise AccountLockedError("Account Locked!")

        except AccountLockedError as e:
            print(e)



obj = LoginSystem()

# Test Logins
obj.login("abc")
obj.login("123")
obj.login("xyz")
obj.login("python@123")