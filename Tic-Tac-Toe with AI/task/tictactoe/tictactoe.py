import random


class TicTacToe:

    def __init__(self):
        self.game_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.remaining_spots = 9
        self.next_mark = {
            "X": "O",
            "O": "X"
        }
        self.win_coords = {
            1: [(0, 0), (0, 1), (0, 2)],  # Row 1
            2: [(1, 0), (1, 1), (1, 2)],  # Row 2
            3: [(2, 0), (2, 1), (2, 2)],  # Row 3
            4: [(0, 0), (1, 0), (2, 0)],  # Column 1
            5: [(0, 1), (1, 1), (2, 1)],  # Column 2
            6: [(0, 2), (1, 2), (2, 2)],  # Column 3
            7: [(0, 0), (1, 1), (2, 2)],  # Diagonal 1
            8: [(2, 0), (1, 1), (0, 2)],  # Diagonal 2
        }

    def show_board(self):
        print("---------")
        for i in self.game_board:
            row = "| "
            for j in i:
                row += j + " "
            print(row + "|")
        print("---------")

    def get_win_conditions(self):
        return {
            1: [self.game_board[0][0], self.game_board[0][1], self.game_board[0][2]],  # Row 1
            2: [self.game_board[1][0], self.game_board[1][1], self.game_board[1][2]],  # Row 2
            3: [self.game_board[2][0], self.game_board[2][1], self.game_board[2][2]],  # Row 3
            4: [self.game_board[0][0], self.game_board[1][0], self.game_board[2][0]],  # Column 1
            5: [self.game_board[0][1], self.game_board[1][1], self.game_board[2][1]],  # Column 2
            6: [self.game_board[0][2], self.game_board[1][2], self.game_board[2][2]],  # Column 3
            7: [self.game_board[0][0], self.game_board[1][1], self.game_board[2][2]],  # Diagonal 1
            8: [self.game_board[2][0], self.game_board[1][1], self.game_board[0][2]],  # Diagonal 2
        }

    def game_over(self, player_mark):
        win_conditions = self.get_win_conditions()
        for cond in win_conditions.values():
            if cond[0] == player_mark and cond[1] == player_mark and cond[2] == player_mark:
                self.remaining_spots = 9
                return player_mark
        if self.remaining_spots == 0:
            self.remaining_spots = 9
            return 0
        return -1

    def place_mark(self, player_mark, mark_coords):
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
        if self.game_board[row][col] != " ":
            print("This cell is occupied! Choose another one!")
            return False
        self.game_board[row][col] = player_mark
        self.remaining_spots -= 1
        return True

    def user_move(self, player_mark):
        coords = input("Enter the coordinates: ").split()
        while not self.place_mark(player_mark, coords):
            coords = input("Enter the coordinates: ").split()

    def ai_easy_move(self, player_mark):
        print('Making move level "easy"')
        self.random_move(player_mark)
        return

    def ai_medium_move(self, player_mark):
        print('Making move level "medium"')
        for cond in self.get_win_conditions().items():
            advance = cond[1].count(player_mark)
            prevent = cond[1].count(self.next_mark[player_mark])
            if advance == 2 and cond[1].count(" ") == 1:
                index = cond[1].index(" ")
                coords = [str(coord + 1) for coord in self.win_coords[cond[0]][index]]
                self.place_mark(player_mark, coords)
                return
            elif prevent == 2 and cond[1].count(" ") == 1:
                index = cond[1].index(" ")
                coords = [str(coord + 1) for coord in self.win_coords[cond[0]][index]]
                self.place_mark(player_mark, coords)
                return
        self.random_move(player_mark)
        return

    def random_move(self, player_mark):
        while True:
            coords = [random.randint(0, 2), random.randint(0, 2)]
            if self.game_board[coords[0]][coords[1]] == " ":
                coords = [str(coords[0] + 1), str(coords[1] + 1)]
                self.place_mark(player_mark, coords)
                return

    def start_game(self, params):
        mark = "X"
        move_sets = {
            "user": self.user_move,
            "easy": self.ai_easy_move,
            "medium": self.ai_medium_move,
            "hard": self.ai_hard_move
        }
        next_turn = {
            1: 2,
            2: 1
        }
        turn = 1
        while True:
            self.show_board()
            move_sets[params[turn]](mark)
            state = self.game_over(mark)
            if state != -1:
                self.show_board()
                if state == mark:
                    print(f"{mark} wins")
                else:
                    print("Draw")
                self.game_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
                return
            mark = self.next_mark[mark]
            turn = next_turn[turn]

    def check_parameters(self, params):
        valid_parameters = ["easy", "medium", "hard", "user", "start", "exit"]
        if params[0] != 'start':
            if "exit" in params:
                exit(0)
            else:
                print("Bad parameters")
                return False
        for param in params:
            if param not in valid_parameters:
                print("Bad parameters")
                return False
        return True


if __name__ == '__main__':
    game = TicTacToe()
    while True:
        parameters = input("Input command: ").split()
        if game.check_parameters(parameters):
            game.start_game(parameters)
