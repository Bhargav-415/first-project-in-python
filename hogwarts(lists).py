"""
students = ["Harry" , "Hermione" , "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])

"""
"""
students = [ "Harry" , "Hermione" , "Ron" , "Draco" ]
houses = [ "Gryffindor" , "Gryffindor" , "Gryffindor" , "Slytherin" ]
"""

"""
students ={ 
    "Harry" : "Gryffindor" , 
    "Hermione" : "Gryffindor", 
    "Ron" : "Gryffindor" , 
    "Draco" : "Slytherin" 
}
for student in students :
    print (student, students[student] , sep = ", ")

"""

students = [
    {"name" : "Hermoine" , "house" : "Gryffindor" , "patronus" : "ottor" },
    {"name" : "Harry" , "house" : "Gryffindor" ,  "patronus" : "stag"},
    {"name" : "Ron"  , "house" : "Gryffindor"  , "patronus" : "jack russele terrier"},
    {"name" : "Ron" , "house" : "Slytherin" , "patronus": None }
]

for student in students :
    print (student["name"] , student ["house"] , student ["patronus"] , sep = ", ")