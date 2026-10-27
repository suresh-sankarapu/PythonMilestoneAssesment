import os
#Employee management System
#FILE_NAME = "employees.txt"
FILE_NAME = os.path.join(os.path.dirname(__file__),"employees.txt")
def create_employee_file():
    with open(FILE_NAME,"w") as file:
        file.write("101,Rahul,Python Developer,50000\n")
        file.write("102,Anjali,Tester,45000\n")
        file.write("103,John,Developer,60000\n")
        file.write("104,Priya,Tester,48000\n")
    print("Employee File created successfully")

class Employee:
    def __init__(self,employee_id,name,role,salary):
        self.employee_id = employee_id
        self.name = name 
        self.role = role
        self.salary = int(salary)

    def display_details(self):
        print(self.employee_id,"-",self.name,"-",self.role,"-",self.salary)

#read employee details from the file
def read_employees():
    employees =[]
    with open(FILE_NAME,"r")as file:
        for line in file:
            data = line.strip().split(",")
            employee = Employee(data[0],data[1],data[2],data[3])
            employees.append(employee)
    return employees

# add a new enmployee
def add_employee(employee_id,name,role,salary):
     with open(FILE_NAME,"a")as file:
          file.write(f"{employee_id},{name},{role},{salary}\n")
          print("employee added successfully")

#5 dislplay all employeess
def dislpay_employees(employees):
     print("\n All employee details:")
     for employee in employees:
      employee.display_details()

#find employees earning more than 50000
def find_employees_by_salary(employees):
        print("\nEmployee earning more than 50000")
        for employee in employees:
            if employee.salary>50000:
                employee.display_details()   

#find employee with the highest salary
def find_highest_salary(employees):
     if len(employees)==0:
        print("N employee records found")   
     highest=max(employees,key=lambda emp:emp.salary)
     print("\nEmployee with the highest salary")
     highest.display_details()

#find employees by role
def find_employees_by_role(employees,role):
     print("\nEmployees in the role:",role)
     found = False
     for employee in employees:
         if employee.role.lower()==role.lower():
             employee.display_details()
             found = True
     if not found:
         print("no employees found for this role")

#count employees by role
def count_employees_by_role(employees):
    role_count={}
    for employee in employees:
        role_count[employee.role]=role_count.get(employee.role, 0)+1
    print("\n Employee count by role")
    for role ,count in role_count.items():
         print(role,":",count)

#create employee file
create_employee_file()
#Read emplotee details once 
employees=read_employees()
#Execute all functiojns
dislpay_employees(employees)
find_employees_by_salary(employees)
find_employees_by_role(employees,"Tester")
find_highest_salary(employees)
count_employees_by_role(employees)
#add_employee(105,"Venkat","Tester",55000)
           