# write your code here
import random

game_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def show_board():
    print("---------")
    for i in game_board:
        row = "| "
        for j in i:
            row += j + " "
        print(row + "|")
    print("---------")


def check_win(player_mark):
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
            print(f"{player_mark} wins")
            return True
    return False


def place_mark(player_mark, mark_coords):
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
    return True


def ai_move(player_mark):
    print('Making move level "easy"')
    while True:
        row, col = random.randrange(0, 3, 1), random.randrange(0, 3, 1)
        if game_board[row][col] == " ":
            game_board[row][col] = player_mark
            return


if __name__ == '__main__':
    mark = "X"
    remaining_spots = 8
    show_board()

    next_mark = {
        "X": "O",
        "O": "X"
    }

    while True:
        coords = input("Enter the coordinates: ").split()
        valid = place_mark(mark, coords)
        while not valid:
            coords = input("Enter the coordinates: ").split()
            valid = place_mark(mark, coords)
        remaining_spots -= 1
        show_board()
        if remaining_spots == 0:
            print("Draw")
            break
        if check_win(mark):
            break
        mark = next_mark[mark]
        ai_move(mark)
        remaining_spots -= 1
        show_board()
        if check_win(mark):
            break
        if remaining_spots == 0:
            print("Draw")
            break
        mark = next_mark[mark]
