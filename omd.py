# Guido van Rossum <guido@python.org>

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
    print ("Вы дали утке зонтик. Но у утки ни лапок, ни ручек. У нее только крылышки. Он не может взять зонтик. Зачем вы дали ей зонтик? Конец.")

def step2_no_umbrella():
    print("Вы не дали утке зонтик. Но на улице ливень. Утке пришлось пить дома одной вместо бара. Почему вы не дали ей зонтик? Конец.")

if __name__ == '__main__':
    step1()