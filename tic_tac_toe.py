gameOver = False
board = [0,0,0,0,0,0,0,0,0]

def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def clearBoard():
    for i in range(9):
        board[i] = 0

def drawBoard():
    for i in range(3):
        print(f"\n {board[3*i]}  {board[3*i+1]}  {board[3*i+2]} ")

def printTieMsg():
    print("\n************************************")
    print("********       TIE GAME!    ********")
    print("************************************")

def checkTie():
    for elem in board:
        if elem == 0:
            return False
    printTieMsg()
    global gameOver
    gameOver = True
    return gameOver

def printWinnerMsg(num):
    print("\n************************************")
    print(f"**  GAME OVER. PLAYER {num} HAS WON!  **")
    print("************************************")

def checkPlayer(num):
    if num == board[0] == board[1] == board[2] or \
       num == board[3] == board[4] == board[5] or \
       num == board[6] == board[7] == board[8] or \
       num == board[0] == board[3] == board[6] or \
       num == board[1] == board[4] == board[7] or \
       num == board[2] == board[5] == board[8] or \
       num == board[0] == board[4] == board[8] or \
       num == board[2] == board[4] == board[6]:
       global gameOver
       gameOver = True
       printWinnerMsg(num)

def checkWinner():
    checkPlayer(1)
    if not gameOver:
        checkPlayer(2)
    return gameOver

def playerMove(n):
    while True:
        pos = input(f"\nPlayer {n}: Enter a position 1-9 for your next move: ")
        if not isInt(pos) or int(pos) < 1 or int(pos) > 9:
            print("\n*** Bad input! Try again! ***\n")
            drawBoard()
            continue

        pos = int(pos)

        if board[pos-1] == 0:
            board[pos-1] = n
            drawBoard()
            break
        else:
            print("\n*** Position already taken! Try again! ***\n")
            drawBoard()

def play():
    while not gameOver:
        playerMove(1)
        if checkTie() or checkWinner():
            break;
        playerMove(2)
        if checkTie() or checkWinner():
            break;

def playGame():
    while True:
        clearBoard()
        print("\n************************************")
        print("****  WELCOME TO TIC TAC TOE!!  ****")
        print("************************************")
        drawBoard()
        play()

        answer = input("Do you want to play again? (y/n): ")
        if answer == "yes" or answer == "y" or answer == "Y" or answer == "Yes" or answer == "YES":
            global gameOver
            gameOver = False
            continue
        elif answer == "no" or answer == "n" or answer == "N" or answer == "No" or answer == "NO":
            print("Thanks for playing! Bye!")
            break
        else:
            print("Unrecognized input. Exiting...Bye!")
            break

playGame()
