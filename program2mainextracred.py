####################################################################################
# Skylar Soehl                                                             10/31/16
#
# Collaboration Statement: I did not work with anyone on this assignment. However,
#                          I did use https://www.youtube.com/watch?v=VfxLL0LdZ_4
#                          as inspiration/a starting point for turtle grphics. In
#                          addition, I used http://vignette1.wikia.nocookie.net/elderscrolls/images/2/24/Michael_Scott_Prison.png/revision/latest?cb=20131114014914
#                          as my player1 piece, http://67.media.tumblr.com/6062f4d2f561c7e209d9b11b2b908066/tumblr_mjmglwSQm01s5c8ivo1_r1_500.png
#                          as my player2 piece, and https://media.glassdoor.com/l/3c/a3/a1/e4/dunder-mifflin-s-bullpen.jpg
#                          as my background and turned each image into a gif using
#                          http://image.online-convert.com/convert-to-gif.
#
# Purpose: to develop a tic-tac-toe game using functions with two players, one
#          represented by 'X' and the other player 'O.' The two players will take
#          turns putting their symbol on a 3 by 3 grid. The first person to get
#          three of their symbols in a line (horrizontal, vertical, diagonal) will
#          win. The program will be able to determine if their is a winner or a
#          tie. 
# Algorithm:
#     1) Create a list called 'board' that contains 9 empty strings
#     2) Create a list called 'locations' that contains string literals of the
#        numbers 1-9 based on the board positions shown in the sample run.
#     3) Print an opening statement to the players and state player 1 will be 'X'
#        and player 2 will be 'O'
#     4) Prompt player 1 and player 2 for their names using the input function and
#        store their reponse to the variables player1 and player2 respectively
#     5) Create a new variable 'player' and set it equal to player 1
#     6) Create 2 new variables, 'player1Symbol' and 'player2Symbol' and set each
#        to a string literal 'X' and 'O', respectively
#     7) Create new variable symbol and set it equal to player1Symbol
#     9) In the #FUNCTION DEFINITIONS section, def the first function as
#        'displayBoard' with the parameter 'board'
#     9) Create a doc string for displayBoard that includes an explanation of
#        the function, the parameters it takes, and what the function returns
#    10) In the function, create a for loop with the range 0 to the length of
#        the board, going by 1 step
#    11) In the for loop if the board equals an empty string, then print a dash
#    12) Else: print board[i], end equal to a string with a space
#    13) Space out the board evenly by creating a if statement that states if i
#        is in index, 2,5,8, then print an empty string
#    14) Print a message to the players telling them to mark their position on the
#        board based on the positions in the same run
#    15) In #MAIN section, invoke displayBoard and pass it locations
#    16) Print a statement telling 'player' that they are starting and that they
#        are playing as 'X'
#    17) Invoke displayBoard and pass it 'board'
#    18) In the #FUNCTION DEFINITIONS section, define a new function called
#        'getMove' with the parameters 'board', 'locations', and 'player'
#    19) Create a doc string for getMove that includes an explanation of the
#        function, the parameters it takes, and what the function returns
#    20) In the function, prompt 'player' for their move and store the reponse
#        into a new variable 'move'
#    21) Turn 'move' into a string
#    22) Create a while loop that will prompt the user for another move as long
#        as the move they entered is not in locations
#    23) Create another while loop (outside the first while loop) that will let
#        the user know that the spot they chose is already taken and prompt them
#        for another move as long as their move does not equal an empty string
#    24) Return move
#    25) In #MAIN section, before board and locations set new variable
#        'gameOver' equal to false
#    26) In #MAIN, after displayBoard(board), create a while loop that will run
#        as long as gameOver is equivalent to False
#    27) In the while loop set invoke getMove and set it equal to move
#    28) In the while loop assign 'symbol' to the index location of the player's
#        move in board
#    29) In the while loop, invoke displayBoard******
#    30) In the #FUNCTION DEFINITIONS section, define a new function win with the
#        the parameters board and symbol
#    31) Create a doc string for win
#    29) Create new variable player_win and set it equal to False
#    30) Create an if statement that will set a new variable 'player_win' equal
#        to true if the index of board at spot 0 is equavalent to symbol AND the
#        the index of board at spot 1 is equavalent to symbol AND the index of
#        board at spot 2 is equavalent to symbol
#    31) Using elif statements, repeat this process for every other win
#        combination (horrizontal, vertical, and diagonal) using the index
#        positions
#    32) Create an else statement that sets player_win to False
#    33) Return player_win
#    34) In #MAIN in the while loop, create an if statement that will print a
#        statement telling the winning player that they won and set gameOver
#        equal to True if the function 'win' is equivalent to True
#    35) In the #FUNCTION DEFINITIONS section, define a new function called tieGame
#        with the parameter 'board'
#    36) Create a dc string for tieGame
#    37) In tieGame, create a new variable called "tie_game" and set it equal to
#        True
#    38) Create a for loop with a range that is the length of board
#    39) In the for loop create an if statement that will flip tie_game from True
#        to False if the index of board at i is equivalent to an empty string
#    40) Return tie_game
#    41) In #MAIN in the while loop, create an elif statement that will print a
#        statement to the players that there is a tie and flip gameOver to True
#        if tieGame is equivalent to True
#    42) In the while loop create an else statement with a nested if loop that
#        will set player equal to player2 and symbol equal to player2Symbol if
#        player is equal to player1
#    43) In the while loop, in the else statement, under/ in line with the nested
#        if statement, create an else statement that will set player equal to
#        player1 and symbol equal to player1Symbol
#    44) Open a new file
#    45) Copy and paste #FUNCTION DEFINITION section into new file
#    46) Save file as Pro2XCredMods.py
#    47) In #MAIN, above gameOver boolean, import Pro2XCredMods
#    48) In #MAIN in front of every invoked function put Pro2XCredMods.thatFunction
#        e.g. (Pro2XCredMods.getBoard())
#    50) In #MAIN import turtle graphics
#    51) Set up turtle screen with 800 by 600 window
#    52) Set up turtle window, name turtle window as 'Program 2: Extra Credit'
#    53) Set background in turtle graphics
#    54) In Pro2XCredMods file, create a define a new function as drawBoard with
#        the parameter turtle
#    55) Create a doc string for drawBoard
#    56) Create a turtle called officeTurtle
#    57) Hide officeTurtle
#    58) Set officeTurtle pen size to 15
#    59) Set officeTurtle pen color to white
#    60) Create first leftmost vertical line of the tic-tac-toe board by:
#          1. picking up the pen,
#          2. setting the position of turtle to (-100, 250)
#          3. pen down
#          4. set position to same x coordinate but negative y
#    61) Repeat (60) for the rightmost vertical line except x coordinate is psotive
#    62) To draw top horrizontal line:
#          1. pen up
#          2. set position to (-275, 100)
#          3. pen down
#          4. turn turtle to the right 0 degrees
#          5. move forward 550
#    63) Repeat (62) for bottom horrizontal line but y coorindate is negative
#    64) In #MAIN under turtle bg pic, invoke drawBoard
#    65) In #MAIN under player1Symbol, player2Symbol register the two images that
#        will be used as the player pieces
#    66) Create two new variables, player1pic and player2pic and set the
#        corresponding image name equal to each variable by putting the name in a
#        string
#    67) Set new variable, playerPic equal to player1pic
#    68) In ProX2CredMods, define a new function as stampBoard with the parameters
#        move, playerPic, and turtle
#    69) Create a doc string for stampBoard
#    70) Create a new turtle and set it equal to 'playerPiece'
#    71) Set playerPiece shape to playerPic
#    72) Put pen up
#    73) Create an if statment that will set playerPiece position inside the first
#        square on the board if move is equivalent to 1
#    74) Create an elif statemet that will set playerPiece position inside the
#        second square on the board elseif move is equivalent to 2
#    75) Repeat (74) for squares 3-9 and moves 3-9 respectively
#    76) Outside the if/elif statements, stamp playerPiece
#    77) In #MAIN, in the while loop, under 'symbol' invoke stampBoard
#     
####################################################################################
#MAIN
import Pro2XCredMods
import turtle

turtle.setup(800, 600)

window = turtle.Screen()

window.title('Program 2 Extra Credit')

turtle.bgpic('dunderMifflin.gif')

Pro2XCredMods.drawBoard(turtle)

gameOver = False
board = ['','','','','','','','','']
locations = ['1','2','3','4','5','6','7','8','9']
#print opening statement with directions
print('Welcome to the tic-tac-toe game!'
      '\nPlayer 1 will be "X" and Player 2 will be "O"')
#get player names
player1 = input('Enter the name of player 1: ')
player2 = input('Enter the name of player 2: ')

player = player1

player1Symbol = 'X'
player2Symbol = 'O'

#player pieces
turtle.register_shape('micheal.gif')
turtle.register_shape('dwight.gif')


player1pic = 'micheal.gif'
player2pic = 'dwight.gif'
playerPic = player1pic


symbol = player1Symbol

print('Enter your mark using the board positions shown below: ')
print('')
#create gameboard w/ #s
Pro2XCredMods.displayBoard(locations)
#greet player one - tell them to start
print('')
print('')
print(player, "you start. You are playing 'X'")

Pro2XCredMods.displayBoard(board)

while gameOver == False:
    move = Pro2XCredMods.getMove(board, locations, player)
    board[int(move)-1] = symbol
    #DR PENCE: Is this what you mean??
    Pro2XCredMods.stampBoard(move, playerPic, turtle)
    #
    Pro2XCredMods.displayBoard(board)
        

    if Pro2XCredMods.win(board,symbol) == True:
        print('Congrats' + ' ' + player + '! You win!!!')
        gameOver = True
        
    elif Pro2XCredMods.tieGame(board) == True:
        print("Dang! It's a tie!")
        turtle.register_shape('tie.gif')
        gameOver = True

    else:
        if player == player1:
            player = player2
            symbol = player2Symbol
            playerPic = player2pic
        else:
            player = player1
            symbol = player1Symbol
            playerPic = player1pic

        
    








