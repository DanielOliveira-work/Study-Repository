import defs_ex10

info = {}

print('-' * 30)
print('Student information'.center(30))
print('-' * 30)
name = input('Type student name: ').title()
student_average = 1
while True:
    grade = float(input(f'Type {student_average}º student grade: '))
    info[student_average] = grade
    option = input('Do you want to continue with a new average?: [S/N] ').lower()[0]
    if option == 'n':
        break
    else:
        student_average += 1
defs_ex10.report_card(info)

