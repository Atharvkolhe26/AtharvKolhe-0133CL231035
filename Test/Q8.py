# Q8. Create a Student Database using JSON: (3 Marks)
# • Create list of 3 students (name, age, city, marks)
# • Save to 'students.json'
# • Read the file and print only students with marks > 75
# • Handle FileNotFoundError

import json

students = {
    "Rahul": 85,
    "Priya": 90,
    "Rohan": 78,
    "Sneha": 92,
    "Amit": 65
}

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("JSON file created successfully.")