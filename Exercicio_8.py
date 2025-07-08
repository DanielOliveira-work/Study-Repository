def record(player, goals):
    if player == '':
        player = '<Unknown>'
    if not goals.isdigit():
        goals = 0
    else:
        goals = int(goals)
    print('-' * 30)
    print(f'The player {player.title()} scored {goals} goals')


player_name = str(input("Player's name: ")).strip()
goals = input('number of goals scored: ')
record(player_name, goals)

