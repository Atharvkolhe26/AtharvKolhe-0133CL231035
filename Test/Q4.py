# 4. Create class AgeVerification: (4 Marks)
# • Method set_age(age):
# fi If age < 0 : raise ValueError
# fi If age < 18 : raise custom UnderAgeError
# fi If age > 100 : raise custom InvalidAgeError
# fi Else : print 'Valid age!'
# Handle all exceptions with finally block.



class UnderAgeError(Exception):
    pass

class InvalidAgeError(Exception):
    pass

class AgeVerification:

    def set_age(self, age):
        try:
            if age < 0:
                raise ValueError("Age is less than 0")
            elif age < 18:
                raise UnderAgeError("Age is less than 18")
            elif age > 100:
                raise InvalidAgeError("Age is greater than 100")
            else:
                print("Valid age!")

        except ValueError as e:
            print(e)

        except UnderAgeError as e:
            print(e)

        except InvalidAgeError as e:
            print(e)

        finally:
            print("Finally block executed")



obj = AgeVerification()

# Test cases
obj.set_age(-5)
obj.set_age(15)
obj.set_age(120)
obj.set_age(25)