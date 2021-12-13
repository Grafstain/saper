import random
SIZE_OF_FIELD = 10
COUNT_MINES = 10

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
    pass

def isFinish():
    """
    isFinish определяет текущее состояние игры:
    выиграли, проиграли, игра продолжается
    """
    pass

def startGame():
    """ startGame функция запуска игры, отображает игровое поле,
        игрок открывает любую закрытую клетку,
        результат проверяется на наличие мины или выигрышной ситуации
    """
    FIELD = [-2]*SIZE_OF_FIELD*SIZE_OF_FIELD
    FIELD_MINES = [0]*SIZE_OF_FIELD *SIZE_OF_FIELD

    # rnd = random.Random()
    # n = COUNT_MINES
    # while n > 0:
    #     i = rnd.randrange(SIZE_OF_FIELD)
    #     j = rnd.randrange(SIZE_OF_FIELD)
    #     print('coordinate', i, j)
    #     print('значение в поле', FIELD_MINES[i][j])
    #     if FIELD_MINES[i][j] == 0:
    #         FIELD_MINES[i][j] = -1
    #         n -= 1
    #         print('n= ', n)
    createGame(FIELD_MINES)
    show(FIELD_MINES)
    # while isFinish():
    #     show()
    #     goPlayer()
    # print(FIELD)
    # print(FIELD_MINES)
startGame()
print("Игра завершена")
