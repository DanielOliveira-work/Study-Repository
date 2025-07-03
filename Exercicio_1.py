#Exercicio com dicionário
def calculo(larg, compr):
    return(larg * compr)


print('Controle de Terrenos')
while True:
    try:
        test_1 = float(input('Digite a largura: '))
        test_2 = float(input('Digite o comprimento: '))
        break
    except ValueError:
        print('Digite um valor correto!')
print(f'A largura do terreto de {test_1} x {test_2} é',calculo(test_1, test_2))





