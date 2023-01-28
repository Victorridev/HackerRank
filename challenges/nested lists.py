numero = int(input())

students = []
    
for i in range(numero):
    name = str(input())
    grade = float(input())
    students.append([name, grade])
students.sort(key=lambda x: (x[0], x[1]))
second_lowest_grade = sorted(set([student[1] for student in students]))[1]
second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]
for name in sorted(second_lowest_students):
    print(name)
# print(tudo_ordenado)
    