import def_conver

price = float(input('ender price: '))
print(f'Half of R${price} is R${def_conver.half(price):.2f}')
print(f'Double R${price} is R${def_conver.double(price):.2f}')
print(f'R${price} with the 10% increase we will have the value of R${def_conver.increase(price):.2f}')
print(f'R${price} with 13% discount we have R${def_conver.discount(price):.2f} ')

