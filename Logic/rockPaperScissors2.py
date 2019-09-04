from random import randint

#Variables
validMoves = ['Rock', 'Paper', 'Scissors']
playerMove = False
points = 0
hearts = 5



def game_logic(validMoves, playerMove, points, hearts):
        while playerMove == False:
            print('You have',hearts , 'hearts and', points, 'points.')
            playerMove = input('Rock, Paper or Scissors? ')
            computerMove = validMoves[randint(0, 2)]
            if hearts <= 0:
                print('Game Over')
                exit
            if playerMove == computerMove:
                print('Computer plays', computerMove)
                print("It's a draw!")
                playerMove = False
            elif playerMove == 'Rock':
                if computerMove == 'Paper':
                    print('Computer plays', computerMove)
                    print('You lose!', computerMove, 'covers', playerMove)
                    playerMove = False
                    hearts -= 1
                else:
                    print('Computer plays', computerMove)
                    print('You win!', playerMove, 'destroys', computerMove )
                    playerMove = False
                    points += 1
            elif playerMove == 'Paper':
                if computerMove == 'Scissors':
                    print('Computer plays', computerMove)
                    print('You lose!', computerMove, 'rips', playerMove)
                    playerMove = False
                    hearts -= 1
                else:
                    print('Computer plays', computerMove)
                    print('You win!', playerMove, 'covers', computerMove )
                    playerMove = False
                    points += 1
            elif playerMove == 'Scissors':
                if computerMove == 'Rock':
                    print('Computer plays', computerMove)
                    print('You lose!', computerMove, 'smashes', playerMove)
                    playerMove = False
                    hearts-= 1
                else:
                    print('Computer plays', computerMove)
                    print('You win!', playerMove, 'shreds', computerMove )
                    playerMove = False
                    points += 1
            else:
                print('Invalid move.')
                playerMove = False


game_logic(validMoves, playerMove, points, hearts)