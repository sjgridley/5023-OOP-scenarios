import grades

students = []

# Creates a dictionary for a student named Michael
# TODO: Change this code to create a Student object, rather than dictionary
michael = {}
michael['name'] = 'Michael'
michael['english_mark'] = 80
michael['science_mark'] = 70
michael['mathematics_mark'] = 70
michael['completed_assessments'] = True
# Adds the dictionary for Michael to the students list
students.append(michael)

# Creates a dictionary for a student named Angela
# TODO: Change this code to create a Student object, rather than dictionary
angela = {}
angela['name'] = 'Angela'
angela['english_mark'] = 60
angela['science_mark'] = 65
angela['mathematics_mark'] = 75
angela['completed_assessments'] = True
# Adds the dictionary for Angela to the students list
students.append(angela)

# Creates a dictionary for a student named Natalie
# TODO: Change this code to create a Student object, rather than dictionary
natalie = {}
natalie['name'] = 'Natalie'
natalie['english_mark'] = 60
natalie['science_mark'] = 65
natalie['mathematics_mark'] = 75
natalie['completed_assessments'] = False
# Adds the dictionary for Natalie to the students list
students.append(natalie)

# Print the names and marks for each of the students
print('\nStudents:\n')
# TODO: Change code in loop to access Student objects' attributes, rather than dictionary
for student in students:
    print('---')
    print(f"Name: { student['name' ]}")
    print(f"English: { student['english_mark'] }")
    print(f"Science: { student['science_mark'] }")
    print(f"Mathematics: { student['mathematics_mark'] }")
    if student["completed_assessments"]:
        print("Completed assessments: Yes")
    else:
        print("Completed assessments: No")
    print('---\n')








