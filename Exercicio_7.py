import math


def factorial_def(value, true_or_not):
    """
    Função de fatorial do valor escolhido pelo usuário. Portugues
    Function factorial the value chosen by the user. English
    :value - valor do calculo fatorial / factorial calculation value 
    :true_or_not - verdadeiro, mostra com calculo. falso, mostra apenas resultado/
                   True, show with calculation. False, show just result.
    """
    factorial_number = math.factorial(value)
    if true_or_not == 'S':
        result = 1
        loop = True
        for number in range(value, 0, -1):
            print(number, end= ' x ' if number > 1 else ' = ') 
            result *= number
        print(result)
    else:
        print(f'O fatorial de {value} é {factorial_number}')


option_while = True
while option_while:
    try:
        value = int(input('Digite o valor do Fatorial desejado: '))
        option = input('Deseja mostrar o calculo? [S/N]: ').upper()[0]
        print(option)
        if option not in ['S', 'N']:
            raise ValueError('Informações inválidas! Por favor, siga as instruções corretas.')
        option_while = False
    except ValueError as erro:
        print(erro)
factorial_def(value, option)