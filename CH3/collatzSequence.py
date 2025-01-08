import sys

def collatz(number):
    while True:
        if number % 2 == 0:
            print(number // 2)
        
        elif number % 2 == 1:
            print(3 * number + 1)

        elif number == 1:
            sys.exit()

collatz(int(input()))