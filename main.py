import random
SIZE_OF_FIELD = 5
COUNT_MINES = 5

def getTotalMines(FIELDS_MINES, i ,j):
    n = 0
    for k in range(-1,2):
        for l in range(-1,2):
            x = i + k
            y = j + l
            if x < 0 or x >= SIZE_OF_FIELD or y < 0 or y >= SIZE_OF_FIELD:
                continue
            if FIELDS_MINES[x*SIZE_OF_FIELD+y] < 0:
                n += 1
    return n

def createGame(FIELD_MINES):
    """
         createGame создает игровое поле,
         подсчитывает количество мин вокруг клеток без мин
    """
    rnd = random.Random()
    n = COUNT_MINES
    while n > 0:
        i = rnd.randrange(SIZE_OF_FIELD)
        j = rnd.randrange(SIZE_OF_FIELD)
        if FIELD_MINES[i*SIZE_OF_FIELD+j] != 0:
            continue
        FIELD_MINES[i*SIZE_OF_FIELD+j] = -1
        n -= 1

    # Вычисляем количество мин вокруг клеток без мин
    for i in range(SIZE_OF_FIELD):
        for j in range(SIZE_OF_FIELD):
            if FIELD_MINES[i*SIZE_OF_FIELD+j] == 0:
                FIELD_MINES[i*SIZE_OF_FIELD+j] = getTotalMines(FIELD_MINES, i, j)


def show(pole):
    """
         Show отображет состояние текущего
         игрового поля
    """
    for i in range(SIZE_OF_FIELD):
        for j in range(SIZE_OF_FIELD):
            print(str(pole[i*SIZE_OF_FIELD+j]).rjust(3), end='')
        print()

def goPlayer():
    """
    goPlayer запрашивает у пользователя координаты закоытой клетки
    игрового поля
    """
    flagrigtinput = True
    while flagrigtinput:
        x, y = input('Введите две координаты через пробел: ').split()
        if not x.isdigit() or not y.isdigit():
            print("Координатты введены неверно")
            continue
        x = int(x) - 1
        y = int(y) - 1

        if x < 0 or x >= SIZE_OF_FIELD or y < 0 or y >= SIZE_OF_FIELD:
            print("Координаты выходят за границы поля")
            continue
        flagrigtinput = False
    return (x,y)

def isFinish(FIELD, FIELD_MINES):
    """
    isFinish определяет текущее состояние игры:
    выиграли, проиграли, игра продолжается
    """
    for i in range(SIZE_OF_FIELD*SIZE_OF_FIELD):
        if FIELD[i] != -2 and FIELD_MINES[i] < 0: return -1
    for i in range(SIZE_OF_FIELD * SIZE_OF_FIELD):
        if FIELD[i] == -2 and FIELD_MINES[i] >= 0: return 1
    return -2


def startGame():
    """ startGame функция запуска игры, отображает игровое поле,
        игрок открывает любую закрытую клетку,
        результат проверяется на наличие мины или выигрышной ситуации
    """
    FIELD = [-2]*SIZE_OF_FIELD*SIZE_OF_FIELD
    FIELD_MINES = [0]*SIZE_OF_FIELD *SIZE_OF_FIELD

    createGame(FIELD_MINES)
    # show(FIELD)
    finishState = isFinish(FIELD, FIELD_MINES)
    while finishState > 0:
        show(FIELD)
        x, y = goPlayer()
        FIELD[x * SIZE_OF_FIELD + y] = FIELD_MINES[x * SIZE_OF_FIELD + y]
        finishState = isFinish(FIELD, FIELD_MINES)
    if isFinish(FIELD, FIELD_MINES) < 0:
        show(FIELD)
    return finishState
res = startGame()
if res == -1:
    print("Вы проиграли!")
else:
    print('Вы выиграли!')
print("Игра завершена")
