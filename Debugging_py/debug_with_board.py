import copy

# aa - препятствие (чужая фигура) ну или своя
# i ->
# j v


board = [
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "aa", "--", "--", "--"],
            ["--", "--", "--", "aa", "--", "--", "--", "--"],
            ["--", "--", "aa", "--", "--", "aa", "--", "--"],
            ["--", "--", "--", "aa", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"]
]

# Логика фигур

def rook(): # wR
    while True:
        # Находим местоположение ладьи
        # Срезы??
        print("Введите координаты белой ладьи")
        i = int(input("i:"))
        j = int(input("j:"))
        b = copy.deepcopy(board)
        b[i][j] = "wR"
        for x in range(0, 8): # i
            for y in range(0, 8): # j
                if (x == i or y == j) and b[x][y] == "--":
                    b[x][y] = "**"
        for i in range(len(b)):
            print(b[i])

rook()

def knight():
    while True:
        print("Введите координаты коня")
        i = int(input("i:"))
        j = int(input("j:"))
        b = copy.deepcopy(board)
        b[i][j] = "wN"
        for x in range(0, 8):  # i
            for y in range(0, 8):  # j
                if (abs(i - x) == 1 and abs(j - y) == 2) or (abs(i - x) == 2 and abs(j - y) == 1):
                    b[x][y] = "**"
        for i in range(len(b)):
            print(b[i])


# knight()

def bishop():
    while True:
        print("Введите координаты слона:")
        i = int(input("i:"))
        j = int(input("j:"))
        b = copy.deepcopy(board)
        b[i][j] = "wB"
        for x in range(0, 8):  # i
            for y in range(0, 8):  # j
                if (abs(x-i) == abs(y-j)) and b[x][y] != "wB":
                    b[x][y] = "**"
        for i in range(len(b)):
            print(b[i])


# bishop()

def king():
    while True:
        print("Введите координаты Короля:")
        i = int(input("i:"))
        j = int(input("j:"))
        b = copy.deepcopy(board)
        b[i][j] = "wK"
        for x in range(0, 8):  # i
            for y in range(0, 8):  # j
                if (abs(x-i) == 1 and abs(y-j) == 1) or (abs(x-i) == 1 and y == j) or (x == i and abs(y-j) == 1):
                    b[x][y] = "**"
        for i in range(len(b)):
            print(b[i])


# king()

def queen():
    while True:
        print("Введите координаты Ферзя:")
        i = int(input("i:"))
        j = int(input("j:"))
        b = copy.deepcopy(board)
        b[i][j] = "wQ"
        for x in range(0, 8):  # i
            for y in range(0, 8):  # j
                if (abs(x-i) == abs(y-j)) and b[x][y] != "wQ" or (x == i or y == j) and b[x][y] == "--":
                    b[x][y] = "**"
        for i in range(len(b)):
            print(b[i])

# queen()


def pawn():
    # логика чёрных. у белых пешек нет
    while True:
        print("Введите координаты пешки:")
        i = int(input("i:"))
        j = int(input("j:"))
        b = copy.deepcopy(board)
        b[i][j] = "wp"
        for x in range(0, 8):  # i
            for y in range(0, 8):  # j
                if j == y and x - i == 1 and b[x][y] == "--":
                    if i == 1:
                        b[x+1][y] = "**"
                    b[x][y] = "**"
        for i in range(len(b)):
            print(b[i])

# pawn()