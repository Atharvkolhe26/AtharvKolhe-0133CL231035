class Employee:
    __salary = 50000
    def increment(self, amount):
        self.__salary +=amount
        print(f"Salary increment: {self.__salary}")

    def deduct(self, amount):
        self.__salary -=amount
        print(f"Salary Deduct: {self.__salary}")

    def get_salary(self):
        print(f"salarys: {self.__salary}")

e1 = Employee()
e1.increment(10000)
e1.deduct(5000)
e1.get_salary()


# . Create a class Employee with: (3 Marks)
# • Private variable __salary = 50000
# • Method increment() fi salary += 10000
# • Method deduct() fi salary -= 5000
# • Method get_salary() fi print salary
# Create 2 objects and call all methods on both.