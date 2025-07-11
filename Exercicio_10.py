def report_card(info):
    """
    :info - student information. 
    """
    bigger = max(info.values()) 
    minor = min(info.values())
    average = (bigger + minor) / len(info)
    if average > 7:
        end_course = 'APROVADO'
    elif 5 < average < 7:
        end_course = 'RECUPERAÇÃO'
    else:
        end_course = 'REPROVADO'
    print(f'The {name} > Test quantities: {len(info)}, highest grade: {bigger}, lowest grade: {minor}, average: {average:.1f} \n{end_course}')

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
report_card(info)