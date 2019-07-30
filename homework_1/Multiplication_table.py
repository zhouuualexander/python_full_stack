def for_1():
    for row in range(1, 10):
        for col in range(1, row + 1):
            print("{}*{}={:<4}".format(row, col, row * col), end=" ")
        print(" ")


def for_2():
    for row in range(9, 0, -1):
        for col in range(1, row + 1):
            print("{}*{}={:<4}".format(row, col, row * col), end=" ")
        print(" ")


def for_3():
    for row in range(1, 10):
        print("    " * (9 - row), end="")
        for col in range(1, row + 1):
            print("{}*{}={:<4}".format(row, col, row * col), end=" ")
        print(" ")


def for_4():
    for row in range(9, 0, -1):
        print("    " * (9 - row), end="")
        for col in range(1, row + 1):
            print("{}*{}={:<4}".format(row, col, row * col), end=" ")
        print(" ")


def for_loop_table():
    print("************以下是用for...in循环构造的九九乘法表************")
    print("")
    print("————————————第一种表现形式————————————")
    for_1()
    print("")
    print("————————————第二种表现形式————————————")
    for_2()
    print("")
    print("————————————第三种表现形式————————————")
    for_3()
    print("")
    print("————————————第四种表现形式————————————")
    for_4()


def while_1():
    row = 0
    col = 1
    while row <= 8:
        row = row + 1
        col = 1
        while col <= row:
            print("{}*{}={:<4}".format(row, col, row * col), end=" ")
            col = col + 1
        print(" ")


def while_2():
    row = 10
    col = 1
    while row >= 1:

        row = row - 1
        col = 1
        while col <= row:
            print("{}*{}={:<4}".format(row, col, row * col), end=" ")
            col = col + 1
        print(" ")


def while_3():
    row = 0
    col = 1
    while row <= 8:

        row = row + 1
        print("    " * (9 - row), end="")
        col = 1
        while col <= row:
            print("{}*{}={:<4}".format(row, col, row * col), end=" ")
            col = col + 1
        print(" ")


def while_4():
    row = 10
    col = 1
    while row >= 1:

        row = row - 1
        print("    " * (9 - row), end="")
        col = 1
        while col <= row:
            print("{}*{}={:<4}".format(row, col, row * col), end=" ")
            col = col + 1
        print(" ")


def while_loop_table():
    print("************以下是用while循环构造的九九乘法表************")
    print("")
    print("————————————第一种表现形式————————————")
    while_1()
    print("")
    print("————————————第二种表现形式————————————")
    while_2()
    print("")
    print("————————————第三种表现形式————————————")
    while_3()
    print("")
    print("————————————第四种表现形式————————————")
    while_4()


def main():
    for_loop_table()
    print("")
    while_loop_table()


main()

