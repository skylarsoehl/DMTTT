def stampBoard(move, playerPic, turtle):

        """This function will use a turtle called playerPiece to stamp the image
           of the corresponding player to the move they chose in locations.

           playerPic must be a string literal containing the image name of the
           player's piece.
           move must be equal to the function getMove and its parameters

           This function is non-value returning.
        """
        
        playerPiece = turtle.Turtle()
        #create new turtle (player piece
        playerPiece.shape(playerPic)
        playerPiece.penup()
        if move == '1':
            playerPiece.setposition(-200, 200)
##        #elif x9
        elif move == '2':
            playerPiece.setposition(0, 200)
        elif move == '3':
            playerPiece.setposition(200, 200)
        elif move == '4':
            playerPiece.setposition(-200, 0)
        elif move == '5':
            playerPiece.setposition(0, 0)
        elif move == '6':
            playerPiece.setposition(200, 0)
        elif move == '7':
            playerPiece.setposition(-200, -200)
        elif move == '8':
            playerPiece.setposition(0, -200)
        elif move == '9':
            playerPiece.setposition(200, -200)
        
        #stamp playerpiece
        playerPiece.stamp()


def drawBoard(turtle):
    """This function will use turtle grpahics to draw two vertical lines of equal
       distance apart and two horrizontal lines equal distance apart to create
       a tic-tac-toe board.

       The function will use turtle, hideTurtle, pensize, pencolor, penup,
       pendown, setposition, right, and forward functions

       This function takes one parameter, turtle

       This function is non-value returning
    """
    officeTurtle = turtle.getturtle()
    officeTurtle.hideturtle()
    officeTurtle.pensize(15)
    officeTurtle.pencolor('white')
    officeTurtle.penup()
    officeTurtle.setposition(250, -25)
    officeTurtle.pendown()

        
    officeTurtle.penup()
    officeTurtle.setposition(-100, 250)
    officeTurtle.pendown()
    officeTurtle.setposition(-100, -250)

    officeTurtle.penup()
    officeTurtle.setposition(100, 250)
    officeTurtle.pendown()
    officeTurtle.setposition(100, -250)

    officeTurtle.penup()
    officeTurtle.setposition(-275, 100)
    officeTurtle.pendown()
    officeTurtle.right(0)
    officeTurtle.forward(550)

    officeTurtle.penup()
    officeTurtle.setposition(-275, -100)
    officeTurtle.pendown()
    officeTurtle.right(0)
    officeTurtle.forward(550)

#tic-tac-toe game

def displayBoard(board):

    """This function will display the tic-tac-toe board and update itself every time
       a player makes a move. The current state of the board depends on the list
       called 'board' that holds the symbols for the board.

       The parameter 'board' mustr be a list that contains strings of the
       symbols 'X' and 'O'. 'Board' will represent the current 9 spaces
       on the board.
       
       This function is non-value returning.
    """
    for i in range(0,len(board),1):
        if board[i] == '':
            print('-', end = ' ')
        else:
            print(board[i], end = ' ')
        if i in(2,5,8):
            print('')

def getMove(board, locations, player):
    
    """This function will prompt the correct player to enter their move and then
       their input back to main.

       The move must be in the list 'locations'.
       
       If the move is not in locations, the function will let the player know
       their move is invalid and prompt the user for another move.
       The move must correspond to a locatoin with an empty string. If the
       location is filled, the function will ask the player to make another move.

       Returns a string literal from the user's move input.
    """
    move = input(player + " enter your move: ")
    move = str(move)
    while move not in(locations):
        move = input('Invalid move! Please enter another move: ')
        
    while board[int(move) - 1] != '':
        move = input('Sorry! That spot is already taken :('
                     '\nMake another move: ')
        
    return move

def win(board, symbol):

    """This function will determine if the current player won with their most
       recent move.

       The parameter 'board' must be a list that contains strings.
       The parameter 'symbol' must be a string variable that reprsents the
       player's corresponding symbol.

       Returns boolean value called 'player_win' which is True if the player won
       and False if not.
    """
#WIN COMBOS
    #horrizontal
    #[1,2,3], [4,5,6], [7,8,9]
    #Vertical
    #[1,4,7], [2,5,8],[3,6,9]
    #Diagonal
    #[1,5,9], [3,5,7]
    player_win = False
    if board[0] == symbol and board[1] == symbol and board[2] == symbol:
        player_win = True
    elif board[3] == symbol and board[4] == symbol and board[5] == symbol:
        player_win = True
    elif board[6] == symbol and board[7] == symbol and board[8] == symbol:
        player_win = True
    elif board[0] == symbol and board[3] == symbol and board[6] == symbol:
        player_win = True
    elif board[1] == symbol and board[4] == symbol and board[7] == symbol:
        player_win = True
    elif board[2] == symbol and board[5] == symbol and board[8] == symbol:
        player_win = True
    elif board[0] == symbol and board[4] == symbol and board[8] == symbol:
        player_win = True
    elif board[2] == symbol and board[4] == symbol and board[6] == symbol:
        player_win = True
    else:
        player_win = False

        
    return player_win

        
def tieGame(board):

    """This function will determine if there is a tied game.

       The parameter 'board' must be a list.

       Returns boolean value called 'tie_game' which is True if the game is a
       tie and False if not.
    """
    tie_game = True
    for i in range(len(board)):
        if board[i] == '':
            tie_game = False
    return tie_game
        














