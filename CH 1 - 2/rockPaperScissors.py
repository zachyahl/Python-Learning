#RPS GAME

import random, sys

wins = 0
losses = 0
ties = 0

while True:
    print('')
    print('ROCK, PAPER, SCISSORS')

# declare win, loss, and tie variables
#    wins = 1
#    losses = 1
#    ties = 1

#display wins, losses, and ties
    print(str(wins) + ' Wins, ' + str(losses) + ' Losses, ' + str(ties) + ' Ties')

    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')

# generate computer variable
# 1 == Rock
# 2 == Paper
# 3 == Scissors
    computerChoice = random.randint(1,3)
    
# accept player choice
    playerChoice = input()

    if playerChoice == 'q':
        sys.exit()
# if player chooses rock
    elif playerChoice == 'r' and computerChoice == 1:
        print('ROCK versus...')
        print('ROCK')
        print('It is a tie!')
        ties = (ties + 1)
        continue

    elif playerChoice == 'r' and computerChoice == 2:
        print('ROCK versus...')
        print('PAPER')
        print('You lose!')
        losses = (losses + 1)
        continue

    elif playerChoice == 'r' and computerChoice == 3:
        print('ROCK versus...')
        print('SCISSORS')
        print('You Win!')
        wins = (wins + 1)
        continue

# if player choses paper
    elif playerChoice == 'p' and computerChoice == 1:
        print('PAPER versus...')
        print('ROCK')
        print('You Win!')
        wins = (wins + 1)
        continue

    elif playerChoice == 'p' and computerChoice == 2:
        print('PAPER versus...')
        print('PAPER')
        print('It is a tie!')
        ties = (ties + 1)
        continue

    elif playerChoice == 'p' and computerChoice == 3:
        print('PAPER versus...')
        print('SCISSORS')
        print('You lose!')
        losses = (losses + 1)
        continue

# if player choses scissors
    elif playerChoice == 's' and computerChoice == 1:
        print('SCISSORS versus...')
        print('ROCK')
        print('You lose!')
        losses = (losses + 1)
        continue

    elif playerChoice == 's' and computerChoice == 2:
        print('SCISSORS versus...')
        print('PAPER')
        print('You Win!')
        wins = (wins + 1)
        continue

    elif playerChoice == 's' and computerChoice == 3:
        print('SCISSORS versus...')
        print('SCISSORS')
        print('It is a tie!')
        ties = (ties + 1)
        continue
    
    else:
        print('Invalid option. Please try again.')
        continue