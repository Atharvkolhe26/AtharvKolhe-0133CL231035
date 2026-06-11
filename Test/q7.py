# Q7. Create an Employee File System: (3 Marks)
# • Create 'employees.txt' with 3 employees
# • Read the file and print
# • Append 2 more employees
# • Read updated file
# • Delete the file and verify using os.path.exists()

with open("employees.txt", "r") as file:
   print(file.read())

with open("employees.txt", "a+") as file:
    file.write("Sneha\n")
    file.write("Amit\n")
with open("employees.txt", "r") as file:
   print(file.read())
