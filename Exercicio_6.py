from datetime import datetime

def year_of_birth(year_user):
    """
    year == age of the user
    """
    time = datetime.now().year
    age = time - year_user
    if age >= 18:
        print(f'Com {age}: VOTO OBRIGATÓRIO.')
    elif 16 <= age < 18:
        print(f'Com {age}: VOTO OPCIONAL.')
    else:
        print(f'Com {age}: NÃO PODE VOTAR.')


year_user = int(input('Em que ano você nasceu?: '))
print(year_of_birth(year_user))
