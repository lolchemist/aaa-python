def step1():
    print(
        'Уткамаляр 🦆 решила погулять. '
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
    print(
        'Какого цвета 🌂 лучше подойдет уткемаляру  🦆?'
    )
    umbrella_color = ''
    color_options = {'красный': '🔴', 'синий': '🔵'}
    while umbrella_color not in color_options:
        print('Выберите: {}/{}'.format(*color_options))
        umbrella_color = input()
    step3_umbrella(color_options[umbrella_color])


def step3_umbrella(color):
    print(
        'Какой красивый  {} ⛱ у уткималяра  🦆?'.format(color),
        'Может, ей прихватить сапоги 👢?️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        print('Отлично! Утка 🦆 пойдет гулять в красивых сапожках 👢 '
              'и с {} ⛱'.format(color))
    else:
        print('Отлично! У утки 🦆 очень красивые лапки 🦵 и {} ⛱'.format(color))


def step2_no_umbrella():
    print('Ну и правиьлно! У 🦆 уже есть водонепроницаемые перышки ☔️')


if __name__ == '__main__':
    step1()
