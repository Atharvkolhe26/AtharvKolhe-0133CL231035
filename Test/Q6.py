# Create a Student Report System: (3 Marks)
# • Create 'report.txt' with 5 students and marks:
# Rahul-85, Priya-90, Rohan-78, Sneha-92, Amit-65
# • Read file and print only students with marks > 80
# • Handle FileNotFoundError with finally block.


    # Create file
file = open("report.txt", "w")
file.write("Rahul-85\n")
file.write("Priya-90\n")
file.write("Rohan-78\n")
file.write("Sneha-92\n")
file.write("Amit-65\n")
file.close()

    # Read file
with open("report.txt", "r") as file:
    for lines in file:
        name , marks = lines.split(" - ")
        if int(marks) > 80:
            print(name, "-", marks)


       