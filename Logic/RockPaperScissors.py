# Rock Paper Scissors in Python
from random import randint

# List of valid moves
moves = ['Rock', 'Paper', 'Scissors']

# AI 
computerMove = moves[randint(0, 2)]

#Player

playerMove = False

while playerMove == False:
    #Set it to true
    playerMove = input('Rock, Paper, Scissors? ')
    if playerMove == computerMove:
        print('Computer plays', computerMove)
        print("It's a draw!")
    elif playerMove == 'Rock':
        if computerMove == 'Paper':
            print('Computer plays', computerMove)
            print('You lose!', computerMove, 'covers', playerMove)
        else:
            print('Computer plays', computerMove)
            print('You win!', playerMove, 'destroys', computerMove )
    elif playerMove == 'Paper':
        if computerMove == 'Scissors':
            print('Computer plays', computerMove)
            print('You lose!', computerMove, 'rips', playerMove)
        else:
            print('Computer plays', computerMove)
            print('You win!', playerMove, 'covers', computerMove )
    elif playerMove == 'Scissors':
        if computerMove == 'Rock':
            print('Computer plays', computerMove)
            print('You lose!', computerMove, 'smashes', playerMove)
        else:
            print('Computer plays', computerMove)
            print('You win!', playerMove, 'shreds', computerMove )
    else:
        print('Invalid move.')
    #To continue the game, we set the player to false now
player = False
computerMove = moves[randint(0, 2)]
    
