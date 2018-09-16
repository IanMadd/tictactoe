import random

playBoard = [1,2,3,4,5,6,7,8,9]
players = {}

def board_display(board):
    print('{0: ^3} | {1: ^3} | {2: ^3}'.format(board[0],board[1],board[2]))
    print('{0: ^3} | {1: ^3} | {2: ^3}'.format(board[3],board[4],board[5]))
    print('{0: ^3} | {1: ^3} | {2: ^3}'.format(board[6],board[7],board[8]))

#input is the players input for a move
#Return: True if the move is an integer from 1:9, False otherwise.
def checkMove(move):
    try:
        move = int(move)
        if move in range(1,10):
            return True
        else:
            return False
    except ValueError:
        print("That is not a number.")
        return False


#input is board and newest move by user
# output True if space NOT previously taken, otherwise false
def checkUnusedSpace(board, move):
    return board[move - 1] != 'X' and board[move - 1] != 'O'

#input current board, user move, and user symbol
#output updated board
def updatedBoard(board, move, userSymbol):
    board[int(move)-1] = userSymbol
    return board

#input player symbol, X or O and current board
# True if current player wins, othewise False
def checkWin(board,userSymbol):

    numberSets = [[0,1,2],[3,4,5],[6,7,8],
                [0,3,6],[1,4,7],[2,5,8],
                [0,4,8],[2,4,6]]

    for set in numberSets:
        if board[set[0]] == userSymbol and board[set[1]] == userSymbol and board[set[2]] == userSymbol:
            return True
            break

    return False

#input board
#output True if all possible moves have been made, otherwise False
def checkDraw(board):
    return all(isinstance(item, str) for item in board)

#input string
#output TRUE if string is either X or O, otherwise False
def checkXO(value):
    try:
        value = str(value)
        if value.upper() == 'X' or value.upper() == 'O':
            return True
        else:
            return False
    except ValueError:
        return False

# output is player not entered in input
def switchPlayer(players, currentPlayer):
    if 'player1' == currentPlayer:
        return 'player2'
    else:
        return 'player1'

def playgame(board, player):
    playing = True
    while playing == True:

        currentPlayerSymbol = list(players.values())[list(players.keys()).index(player)]['userSymbol']
        currentPlayerName = list(players.values())[list(players.keys()).index(player)]['name']

        print('\n'*2)
        print('The board looks like this:')
        print(currentPlayerName + " it's your move.")
        print('You play ' + currentPlayerSymbol)
        board_display(board)

        goodmove = False
        while goodmove == False:
            move = input('Pick an unused space on the board between 1 and 9: ')
            if checkMove(move) == True and checkUnusedSpace(board,int(move)) == True:
                goodmove = True

        board = updatedBoard(board=board, move=move, userSymbol=currentPlayerSymbol)

        if checkWin(board,currentPlayerSymbol) == True:
            print('\n'*2)
            print("Congratulations " + currentPlayerName + " wins!")
            playing = False

        elif checkDraw(board):
            print('\n'*2)
            print('This game is a draw')
            playing = False

        else:
            player = switchPlayer(players=players, currentPlayer=player)

### Begin Tic Tac Toe Game ----------------------------------------------------

print('\n'*5)

print("Ready to play tic-tac-toe?")

print('\n')

players={'player1' : {}, 'player2' : {}}

players['player1']['name'] = input("Player1: What is your name? ")
players['player2']['name'] = input("Player2: What is your name? ")

requestXO = False
while requestXO == False:
    print('\n')
    playerRequest = input(players['player1']['name'] + ': Would you like to be X or O? ')
    requestXO = checkXO(playerRequest)

players['player1']['userSymbol'] = playerRequest.upper()

if playerRequest.upper() == 'X':
    players['player2']['userSymbol'] = 'O'
else:
    players['player2']['userSymbol'] = 'X'

print('\n')

currentPlayer = random.choice(list(players.keys()))

print(list(players.values())[list(players.keys()).index(currentPlayer)]['name'] + ' has been randomly selected to play first.')

playgame(playBoard,currentPlayer)

board_display(playBoard)
