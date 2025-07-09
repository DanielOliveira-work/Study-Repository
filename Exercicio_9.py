def validation(number):
    """
    :number - validation if number is whole value.
    """
    print('-' * 30)
    while True:
        if not number.isdigit():
            print('Error!! Type a whole number valided')
            number = input('Type value: ')
        else:
            return number

number = validation(input('Type value: '))
print(f'Do you typed the number: {number}')