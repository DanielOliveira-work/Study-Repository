import time

def bigger(*numb):
    print('Análisando valores encontrados...')
    for index, number in enumerate(numb):
        if index == 0 or number >= bigger_number:
            bigger_number = number
        print(number, end=' ')
        time.sleep(0.5)
    if len(numb) > 1:
        print(f'Foram informados {len(numb)} valores ao total')
    print(f'O maior número foi {bigger_number}')
    print('-=' * 30)


#programa principal
bigger(5, 9, 2, 8, 7)
bigger(7, 4, 0)
bigger(0)