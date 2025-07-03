import time

def counter(start, end, steps):
    counter = sum_numb = 0
    print('-=' * 30)
    print(f'Contagem de {start} até {end} de {steps} em {steps}')
    if start <= end:
        while start <= end:
            time.sleep(0.5)
            print(start, end=' ') # 1
            start += steps
        print('FIM')
    elif start >= end:
        while start >= end:
            time.sleep(0.5)
            print(start, end=' ')
            start -= abs(steps)
        print('FIM')

counter(1, 10, 1)
counter(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
start = int(input('Inicio: '))
end = int(input('Fim: '))
steps = int(input('Passo: '))
counter(start, end, steps)

