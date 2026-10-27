#student marks  management
from playwright.sync_api import expect
#calculate the totalmarks ,Averagemarks and grade.
def student_grade(average):
    if average>=75:
        return "A"
    elif average>=60:
        return "B"
    elif average >=40:
        return "C"
    else :
        return "F"

students =[{"id":101,"name":"Rahul","python":85,"sql":75,"Ai":80},
             {"id":102,"name":"Anjali","python":70,"sql":60,"Ai":65},
             {"id":103,"name":"priya","python":90,"sql":85,"Ai":95},
             {"id":104,"name":"Suresh","python":50,"sql":45,"Ai":55}]
print("======Student results=======\n")

for student in students:
    total = student["python"]+student["sql"]+student["Ai"]
    average = total/3
    grade = student_grade(average)
    if average >=40: 
        result = "PASS"
    else:
        result=  "Fail"
    student["average"]=average
    student["total"]=total
    student["grade"]=grade
    student["result"]=result

    print("student_name" ,student["name"])
    print("student_id" ,student["id"])
    print("total" ,student["total"])
    print("avg",round(student["average"],2))
    print("grade",student["grade"])
    print("result",student["result"])
    print()

#highest averag student name
highest_student  = students[0]
for student in students:
    if student["average"]>highest_student["average"]:
        highest_student = student
print("Highest Scoring student:",highest_student["name"])


#list comprehension
top_students = [
    student["name"]
    for student in students
    if student["average"] >75
]

print("students above 75:",top_students)