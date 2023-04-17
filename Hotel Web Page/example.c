x = int(input("Enter the value of x: "))

y = int(input("Enter the value of y: "))

g = int(input("Enter the value of g: "))

def print_jugs(a, b, c):
    print("="*5)
    print("Jug X: {}, Jug Y: {}, Moves: {}".format(a, b, c))
    print("="*5)

x_filled, y_filled, moves = 0, 0, 0

while(True):

    print_jugs(x_filled, y_filled, moves)

    if(x_filled == g and y_filled == 0 or x_filled == 0 and y_filled == g):
        print("\nCongrats! You won!!")
        print_jugs(x_filled, y_filled, moves)
        break

    print("1.Empty Jug X\n2.Empty Jug Y\n3.Transfer from X to Y\n4.Transfer from Y to X\n5.Fill Jug X\n6.Fill Jug Y")
    ch = int(input("Enter Choice: "))

    if(ch == 1):
        x_filled = 0
    elif(ch == 2):
        y_filled = 0
    elif(ch == 3):
        while(y_filled != y and x_filled != 0):
            x_filled -= 1
            y_filled += 1
    elif(ch == 4):
        while(y_filled != 0 and x_filled != x):
            x_filled += 1
            y_filled -= 1
    elif(ch == 5):
        x_filled = x
    elif(ch == 6):
        y_filled = y
    else:
        print("Error!")

    moves += 1