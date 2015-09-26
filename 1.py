import json


Class = '6 А' # input("класс(5а, 6а,7г, 6г, 8д):")
teach = open("Teachers.json")
T_data = json.load(teach)
stud = open('Students.json')
S_data = json.load(stud)
school = []

for S_name in S_data:
    name = S_name['name']
    print("Ученик:", name)


for T_name in T_data:
    T_name = T_name['name']
    print("Учитель:", T_name)


for Class1 in S_data:
    C = Class1['class']
    print(C)


for F_name in S_data:
    qname = F_name['name']
    ename = F_name['surname']
    print(qname, ename)


for school1 in S_data:
    s = school1['school']
    print(s)
