import random

# Rules


def field4():
    field = [1, 2, 3, 4,
             5, 6, 7, 8,
             9, 10, 11, 12,
             13, 14, 15, 16]
    bomb = random.randint(0, 15)

    def show_board():
        print(field[0], " |", field[1], " |", field[2], " |", field[3])
        print(field[4], " |", field[5], " |", field[6], " |", field[7])
        print(field[8], " |", field[9], "|", field[10], "|", field[11])
        print(field[12], "|", field[13], "|", field[14], "|", field[15])
    show_board()
    while True:
        player = int(input("Pick a block number: "))
        if (player - 1) == bomb:
            print("Oops,You stepped on a bomb")
            field[player - 1] = "X"
            show_board()
            break
        else:
            print("Good choice")
            field[player - 1] = " "
            show_board()


field4()
