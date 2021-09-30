import grades

michael = grades.Student (
        name = 'Michael',
        english_mark = 80,
        science_mark = 70,
        mathematics_mark = 70,
        completed_assessments = True
    )

angela = grades.Student (
        name = 'Angela',
        english_mark = 60,
        science_mark = 65,
        mathematics_mark = 75,
        completed_assessments = True
    )

natalie = grades.Student (
        name = 'Natalie',
        english_mark = 60,
        science_mark = 65,
        mathematics_mark = 75,
        completed_assessments = False
    )

students = [michael, angela, natalie]
print('\nStudents:\n')

for student in students:
    print('---')
    print(f"Name: {student.name}")
    print(f"English: {student.english_mark}")
    print(f"Science: {student.science_mark}")
    print(f"Mathematics: {student.mathematics_mark}")
    print(f'Average mark: {student.average_mark()}')
    if student.completed_assessments:
        print("Completed assessments: Yes")
    else:
        print("Completed assessments: No")
    print('---\n')








