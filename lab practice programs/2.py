print("By 22IT460")
students = {
    "Avadh": 85,
    "Darpit": 92,
    "Sagar": 78,
    "Neel": 95,
    "Pratham": 88
}
top_student = None
highest_marks = -1
for student in students:
    if students[student] > highest_marks:
        highest_marks = students[student]
        top_student = student
print("Top performer:", top_student)