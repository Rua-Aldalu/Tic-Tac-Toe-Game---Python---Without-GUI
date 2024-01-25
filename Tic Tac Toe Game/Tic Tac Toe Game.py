# TIC TAC TOE GAME
# Function to collect player information
def players():
    player1 = []
    player2 = []
    for i in range(2):
        if i == 0:
            name = name_correction()
            player1.append(name.upper())
            symbol = input("Enter Your Chosen Symbol X or O: ")
            symbol = symbol.upper()
            while symbol != "O" and symbol != "X":
                print("Please Enter Only X or O Letter")
                symbol = input("Enter Your Chosen Symbol X or O: ")
                symbol = symbol.upper()
            player1.append(symbol)
        else:
            name = name_correction()
            player2.append(name.upper())
            if player1[1] == "X":
                player2.append("O")
            else:
                player2.append("X")
    return player1, player2


# Function to ensure a valid name
def name_correction():
    while True:
        try:
            name = input("Enter The Player's Name: ")
            if not name.isalpha():
                raise ValueError("Please Only Enter Letters as a Name")
            break
        except ValueError as error:
            print(error)
    return name


# Function to display the Tic Tac Toe board
def game_board(player1, player2, board_cells):
    print("\n\n              Tic Tac Toe Game              ")
    print("\nFirst Player: ", player1[0], "      Second Player: ", player2[0])
    print(player1[0], "Symbol: ", player1[1], "         ", player2[0], "Symbol: ", player2[1], "\n")
    counter = 0
    for i in range(3):
        if counter == 0:
            for j in range(3):
                print(board_cells[j], end=' ')
            print("\n")
            counter += 1
        elif counter == 1:
            for j in range(3, 6):
                print(board_cells[j], end=' ')
            print("\n")
            counter += 1
        else:
            for j in range(6, 9):
                print(board_cells[j], end=' ')
            print("\n")
            counter += 1


# Function to handle player moves
def playing(player):
    global cell_position
    global board_cells

    while True:
        try:
            chosen_cell = int(input(f"{player[0]} Please Enter The Number of your chosen cell "))
            break
        except ValueError:
            print("Please Enter Only a Number Not Any Letter or Symbol")

    while chosen_cell <= 0 or chosen_cell > 9:
        print("Please Enter Only A Cell Number From 1 to 9 ")
        chosen_cell = int(input(f"{player[0]} Please Enter The Number of your chosen cell "))

    while cell_position[str(chosen_cell)] == "   X  " or cell_position[str(chosen_cell)] == "   O  ":
        print("Please This Cell Is Already Played, Choose Another Cell")
        chosen_cell = int(input(f"{player[0]} Please Enter The Number of your chosen cell "))

    player_symbol = player[1]
    player_symbol = "   " + player_symbol + "  "
    cell_position[str(chosen_cell)] = player_symbol
    board_cells = []
    for key in cell_position:
        board_cells.append(cell_position[key])
    game_board(player1, player2, board_cells)


# Function to check for a tie
def tie(board_cells):
    flag = True
    for cell in board_cells:
        if cell == "   X  " or cell == "   O  ":
            flag = flag
        else:
            flag = not flag
            break
    return flag


# Function to check for a win
def winning(board_cells, player_symbol):
    wining_cases = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]

    for case in wining_cases:
        for cell in case:
            if board_cells[cell] == player_symbol:
                flag = True
            else:
                flag = False
                break
        if flag == True:
            break
    return flag


# Main game loop
rounds_counter = 1
while True:
    (player1, player2) = players()
    #default_cell = " | ___ |"
    cell_position = {"1":  "   1  ", "2":  "   2  ", "3":  "   3  ",
                     "4": "   4  ", "5": "   5  ", "6": "   6  ",
                     "7": "   7  ", "8": "   8  ", "9" : "   9  "}
    board_cells = []
    for key in cell_position:
        board_cells.append(cell_position[key])
    game_board(player1, player2, board_cells)

    flag = True
    while True:
        its_tie = tie(board_cells)
        if its_tie == False:
            if flag == True:
                playing(player1)
                player_symbol = "   " + player1[1] + "  "
                its_winning = winning(board_cells, player_symbol)
                if its_winning == True:
                    print(f"Congrats, {player1[0]} you Won The Game")
                    break
            else:
                playing(player2)
                player_symbol = "   " + player2[1] + "  "
                its_winning = winning(board_cells, player_symbol)
                if its_winning == True:
                    print(f"Congrats, {player2[0]} you Won The Game")
                    break
            flag = not flag
        else:
            print("Game Over, None Has Won The Game")
            break
    replay = input("Do you Wanna Play Again?, Answer Y Or N: ")
    replay = replay.upper()
    while True:
        if replay == "Y" or replay == "N":
            break
        else:
            print("Please Enter Only Y Or N")
            replay = input("Do you Wanna Play Again?, Answer Y Or N: ")
            replay = replay.upper()

    if replay == "N":
        break
    else:
        rounds_counter += 1
        print(f"\n      Let's Play and Have Fun Again      \n                ROUND {str(rounds_counter)}      \n")
