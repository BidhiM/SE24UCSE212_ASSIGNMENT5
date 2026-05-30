from copy import deepcopy
import random
import math

class TicTacToe:
    
    def __init__(self, cells=None, turn='X'):
        self.cells = cells if cells else ['.'] * 9
        self.turn = turn

    def possible_moves(self):
        return [index for index, value in enumerate(self.cells) if value == '.']

    def apply_move(self, position):

        updated_board = deepcopy(self.cells)
        updated_board[position] = self.turn

        next_turn = 'O' if self.turn == 'X' else 'X'

        return TicTacToe(updated_board, next_turn)

    def check_winner(self):

        winning_sets = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]

        for pattern in winning_sets:
            x, y, z = pattern

            if self.cells[x] == self.cells[y] == self.cells[z] != '.':
                return self.cells[x]

        if '.' not in self.cells:
            return 'Draw'

        return None

    def game_over(self):
        return self.check_winner() is not None

    def score(self):

        result = self.check_winner()

        if result == 'X':
            return 1

        if result == 'O':
            return -1

        return 0

    def display(self):

        for row in range(0, 9, 3):
            print(self.cells[row:row+3])

        print()


class MinimaxAgent:

    def minimax(self, state, maximizing):

        if state.game_over():
            return state.score()

        if maximizing:

            best = -float('inf')

            for move in state.possible_moves():

                value = self.minimax(
                    state.apply_move(move),
                    False
                )

                best = max(best, value)

            return best

        else:

            best = float('inf')

            for move in state.possible_moves():

                value = self.minimax(
                    state.apply_move(move),
                    True
                )

                best = min(best, value)

            return best

    def best_move(self, state):

        best_score = -float('inf')
        move_choice = None

        for move in state.possible_moves():

            score = self.minimax(
                state.apply_move(move),
                False
            )

            if score > best_score:
                best_score = score
                move_choice = move

        return move_choice


state = TicTacToe(

    cells=[
        'X','X','.',
        'O','O','.',
        '.','.','.'
    ],

    turn='X'
)

print("Initial Board")
state.display()

minimax_agent = MinimaxAgent()

print(
    "Best move using Minimax:",
    minimax_agent.best_move(state)
)
