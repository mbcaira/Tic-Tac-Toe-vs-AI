# write your code here
import random

game_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
remaining_spots = 9
next_mark = {
    "X": "O",
    "O": "X"
}
win_coords = {
    1: [(0, 0), (0, 1), (0, 2)],  # Row 1
    2: [(1, 0), (1, 1), (1, 2)],  # Row 2
    3: [(2, 0), (2, 1), (2, 2)],  # Row 3
    4: [(0, 0), (1, 0), (2, 0)],  # Column 1
    5: [(0, 1), (1, 1), (2, 1)],  # Column 2
    6: [(0, 2), (1, 2), (2, 2)],  # Column 3
    7: [(0, 0), (1, 1), (2, 2)],  # Diagonal 1
    8: [(2, 0), (1, 1), (0, 2)],  # Diagonal 2
}


def show_board():
    print("---------")
    for i in game_board:
        row = "| "
        for j in i:
            row += j + " "
        print(row + "|")
    print("---------")


def get_win_conditions():
    return {
        1: [game_board[0][0], game_board[0][1], game_board[0][2]],  # Row 1
        2: [game_board[1][0], game_board[1][1], game_board[1][2]],  # Row 2
        3: [game_board[2][0], game_board[2][1], game_board[2][2]],  # Row 3
        4: [game_board[0][0], game_board[1][0], game_board[2][0]],  # Column 1
        5: [game_board[0][1], game_board[1][1], game_board[2][1]],  # Column 2
        6: [game_board[0][2], game_board[1][2], game_board[2][2]],  # Column 3
        7: [game_board[0][0], game_board[1][1], game_board[2][2]],  # Diagonal 1
        8: [game_board[2][0], game_board[1][1], game_board[0][2]],  # Diagonal 2
    }


def game_over(player_mark):
    global remaining_spots
    win_conditions = get_win_conditions()
    for cond in win_conditions.values():
        if cond[0] == player_mark and cond[1] == player_mark and cond[2] == player_mark:
            remaining_spots = 9
            return 1
    if remaining_spots == 0:
        remaining_spots = 9
        return 0
    return -1


def place_mark(player_mark, mark_coords):
    global remaining_spots
    global game_board
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
    random_move(player_mark)
    return


def ai_medium_move(player_mark):
    print('Making move level "medium"')
    for cond in get_win_conditions().items():
        advance = cond[1].count(player_mark)
        prevent = cond[1].count(next_mark[player_mark])
        if advance == 2 and cond[1].count(" ") == 1:
            index = cond[1].index(" ")
            coords = [str(coord+1) for coord in win_coords[cond[0]][index]]
            place_mark(player_mark, coords)
            return
        elif prevent == 2 and cond[1].count(" ") == 1:
            index = cond[1].index(" ")
            coords = [str(coord+1) for coord in win_coords[cond[0]][index]]
            place_mark(player_mark, coords)
            return
    random_move(player_mark)
    return


def ai_hard_move(player_mark):
    pass


def random_move(player_mark):
    while True:
        coords = [random.randint(0, 2), random.randint(0, 2)]
        if game_board[coords[0]][coords[1]] == " ":
            coords = [str(coords[0] + 1), str(coords[1] + 1)]
            place_mark(player_mark, coords)
            return


def start_game(params):
    global game_board
    mark = "X"
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
        state = game_over(mark)
        if state == 1 or state == 0:
            show_board()
            if state == 1:
                print(f"{mark} wins")
            else:
                print("Draw")
            game_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
            return
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
