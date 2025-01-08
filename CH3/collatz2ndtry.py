import sys

def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(number // 2)
            continue

        elif number % 2 == 1:
            number = 3 * number + 1
            print(3 * number + 1)
            continue
    else:
        sys.exit()

while True:

    print('Enter a Number.')

    playerInput = input()
    
    try:
        collatz(int(playerInput))

    except ValueError:
        print('Player must enter an integer value.')


        

