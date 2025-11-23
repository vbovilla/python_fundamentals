
contacts = {
    'number': 4,
    'students':
    [
        {'name': 'Vishnu Vardhan', 'email': 'vishnu_vardhan@tjx.com'},
        {'name': 'Harini Bovilla', 'email': 'harini.bovilla@gmail.com'},
        {'name': 'Vihari Bovilla', 'email': 'vihari.bovilla@gmail.com'},
        {'name': 'Vishnu Bovilla', 'email': 'vishnu.bovilla@gmail.com'}
    ]
}
print(contacts)

students_emails = []
print('Student Details:\n')
for student in contacts['students']:
    email = student['email']
    # print(email)
    students_emails.append(email)

print(students_emails)
