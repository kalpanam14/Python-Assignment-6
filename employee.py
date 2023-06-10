import json

# #define the employee class
class Employee:
     def __init__(self, name, dob, height, city, state):
         self.name = name
         self.dob = dob
         self.height = height
         self.city = city
         self.state = state

fileObj = open(r"/Volumes/BiBiLo/Python/Code/assignment/employees.json")

# #load the file
employee_data = json.load(fileObj)

# # Extract employee information from the dictionary and create Employee objects
employees = []

for emp in employee_data["employees"]:
     name = emp["name"]
     dob = emp["dob"]
     height = emp["Height"]
     city = emp["city"]
     state = emp["state"]
     employee = Employee(name, dob, height, city, state)
     employees.append(employee)

for emp in employees:
     print("Name : ", emp.name)
     print("DOB : ", emp.dob)
     print("Height : ", emp.height)
     print("City : ", emp.city)
     print("State : ", emp.state)
