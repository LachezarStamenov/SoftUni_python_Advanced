# Write a program, which reads a name of a student and their grades and adds them to the student record.
# Print the name of the students with their grades and their average grade.
# The order in which we print the result does not matter.


student_num = int(input())
students = {}

for i in range(student_num):
    name, grade = input().split()
    grade = float(grade)
    if name not in students:
        students[name] = []
    students[name].append(grade)
for data in students.items():
    print(f"{data[0]} -> {' '.join(f'{x:.2f}' for x in data[1])} (avg: {(sum(data[1])/len(data[1])):.2f})")
