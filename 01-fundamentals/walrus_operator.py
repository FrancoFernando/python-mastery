def walrus_dictionary():

    fruits = {
        'apple': 2,
        'lemon ': 12,
        'orange': 10,
    }

    count = fruits.get('orange', 0)
    if count > 3:
        to_drink = make_orange_juice(count)
    else:
        count = fruits.get('lemon', 0)
        if count > 2:
            to_drink = make_lemon_juice(count)
        else:
            to_drink = 'no drink'

    if (count := fruits.get('orange', 0)) >= 3:
        to_drink = make_orange_juice(count)
    elif (count := fruits.get('lemon', 0)) >= 2:
        to_drink = make_lemon_juice(count)
    else:
        to_drink = 'no drink'

    
def make_orange_juice(count):
    print('orange juice')

def make_lemon_juice(count):
    print('lemon juice')


def walrus_dowhile():

    #do/while without walrus
    n = 1
    while True:
        print(n)
        n = n + 1
        if (n > 3):
            break

    #do/while with walrus
    n = 0
    while (n := n + 1) <= 3:
        print(n)