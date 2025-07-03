from random import randint
import time

def draw(numb):
    lista = []
    print(f'Sorteando 5 valores da lista: ', end='')
    for count in range(0, 5):
        whole = randint(1,10)
        lista.append(whole)
        print(f'{whole}', end=' ')
        time.sleep(0.5)   
    print('PRONTO!!!!', end='\n')
    return(lista)

def adding_pairs(list_number):
    sum = 0
    for number in list_number:
        if number % 2 == 0:
            sum += number
    print(f'Somando os valores pares de {list_number}, temos {sum}')


lista = draw(5)
adding_pairs(lista)