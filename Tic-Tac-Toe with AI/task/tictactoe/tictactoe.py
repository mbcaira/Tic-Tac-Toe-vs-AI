# write your code here
import random

game_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
remaining_spots = 8


def show_board():
    print("---------")
    for i in game_board:
        row = "| "
        for j in i:
            row += j + " "
        print(row + "|")
    print("---------")


def game_over(player_mark):
    win_conditions = {
        1: [game_board[0][0], game_board[0][1], game_board[0][2]],  # Row 1
        2: [game_board[1][0], game_board[1][1], game_board[1][2]],  # Row 2
        3: [game_board[2][0], game_board[2][1], game_board[2][2]],  # Row 3
        4: [game_board[0][0], game_board[1][0], game_board[2][0]],  # Column 1
        5: [game_board[0][1], game_board[1][1], game_board[2][1]],  # Column 2
        6: [game_board[0][2], game_board[1][2], game_board[2][2]],  # Column 3
        7: [game_board[0][0], game_board[1][1], game_board[2][2]],  # Diagonal 1
        8: [game_board[2][0], game_board[1][1], game_board[0][2]],  # Diagonal 2
    }
    for cond in win_conditions.values():
        if cond[0] == player_mark and cond[1] == player_mark and cond[2] == player_mark:
            show_board()
            print(f"{player_mark} wins")
            exit(0)
    if remaining_spots == 0:
        print("Draw")
        exit(0)


def place_mark(player_mark, mark_coords):
    global remaining_spots
    valid_coords = ["1", "2", "3"]
    try:
        row = int(mark_coords[0]) - 1
        col = int(mark_coords[1]) - 1
    except ValueError:
        print("You should enter numbers!")
        return False

    if mark_coords[0] not in valid_coords or mark_coords[1] not in valid_coords:
        print("Coordinates should be from 1 to 3!")
        return False
    if game_board[row][col] != " ":
        print("This cell is occupied! Choose another one!")
        return False
    game_board[row][col] = player_mark
    remaining_spots -= 1
    return True


def user_move(player_mark):
    coords = input("Enter the coordinates: ").split()
    while not place_mark(player_mark, coords):
        coords = input("Enter the coordinates: ").split()


def ai_easy_move(player_mark):
    print('Making move level "easy"')
    while True:
        coords = [random.randrange(0, 3, 1), random.randrange(0, 3, 1)]
        if game_board[coords[0]][coords[1]] == " ":
            place_mark(player_mark, coords)
            return


def ai_medium_move(player_mark):
    pass


def ai_hard_move(player_mark):
    pass


def start_game(params):
    mark = "X"
    next_mark = {
        "X": "O",
        "O": "X"
    }

    move_sets = {
        "user": user_move,
        "easy": ai_easy_move,
        "medium": ai_medium_move,
        "hard": ai_hard_move
    }
    next_turn = {
        1: 2,
        2: 1
    }
    turn = 1
    while True:
        show_board()
        move_sets[params[turn]](mark)
        game_over(mark)
        mark = next_mark[mark]
        turn = next_turn[turn]


def check_parameters(params):
    valid_parameters = ["easy", "medium", "hard", "user"]
    if params[0] != 'start':
        return False
    for param in params[1:]:
        if param not in valid_parameters:
            return False
    return True


if __name__ == '__main__':
    while True:
        parameters = input("Input command: ").split()
        if "exit" in parameters:
            exit(0)
        if check_parameters(parameters):
            start_game(parameters)
        else:
            print("Bad parameters")
