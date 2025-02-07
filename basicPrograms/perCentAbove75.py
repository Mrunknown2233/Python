
#making a list of dictionary for students
students = [ 
          {"rollNo" : 1 ,"name" : "Soumya", "percentage" : 89.88},
          {"rollNo" : 2 ,"name" : "Abc","percentage" : 75},
          {"rollNo" : 3 ,"name" : "PQR","percentage" : 70},
          {"rollNo" : 4 ,"name" : "asd","percentage" : 75.1}
]

print(list(map(lambda student : student["name"],list(filter(lambda student : student["percentage"]>=75,students)))))


