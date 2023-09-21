# Guido van Rossum <guido@python.org>
import random

def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    
    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()

def step2_umbrella():
    print('Вы решили дать утке зонтик. Она вас благодарит и идет в бар.')
    if random.choice([True, False]):  # Решаем, будет ли дождь
        print('На улице пошел дождь. Утка с зонтиком осталась сухой.')
    else:
        print('На улице сегодня без дождя. Утка радуется своему зонтику.')

def step2_no_umbrella():
    print('Вы решили не давать утке зонтик. Утка идет в бар без него.')
    if random.choice([True, False]):  # Решаем, будет ли дождь
        print('На улице пошел дождь. Утка без зонтика промокла.')
    else:
        print('На улице сегодня без дождя. Утка радуется, что не взяла зонтик.')

if __name__ == '__main__':
    step1()