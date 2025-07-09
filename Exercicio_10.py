def report_card(info):
    #total, maior, menor, média e se foi aprovado com boleano.
    bigger = minor = total = 0
    for itens, value in info.items():
        total += value
        if itens == 0 or value > bigger:
           bigger = value
        if itens == 0:
            minor == value
    average = total / len(info) 
    print(f'The {name} > Test quantities: {len(info)}, highest grade: {bigger}, lowest grade: {minor}, average: {average}')

##CONTINUAR AMANHA, TRUE OR FALSE 

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