
from copy import deepcopy
import random
import math


class TicTacToe:

    def __init__(self, cells=None, turn='X'):

        self.cells = cells if cells else ['.'] * 9
        self.turn = turn

    def possible_moves(self):

        return [
            index
            for index, value in enumerate(self.cells)
            if value == '.'
        ]

    def apply_move(self, position):

        updated = deepcopy(self.cells)

        updated[position] = self.turn

        next_turn = 'O' if self.turn == 'X' else 'X'

        return TicTacToe(updated, next_turn)

    def check_winner(self):

        winning_patterns = [

            [0,1,2],
            [3,4,5],
            [6,7,8],

            [0,3,6],
            [1,4,7],
            [2,5,8],

            [0,4,8],
            [2,4,6]
        ]

        for pattern in winning_patterns:

            a, b, c = pattern

            if self.cells[a] == self.cells[b] == self.cells[c] != '.':
                return self.cells[a]

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

        print()

        for row in range(0, 9, 3):

            print(
                self.cells[row],
                "|",
                self.cells[row+1],
                "|",
                self.cells[row+2]
            )

        print()
class AlphaBetaAgent:

    def alphabeta(
        self,
        state,
        alpha,
        beta,
        maximizing
    ):

        if state.game_over():
            return state.score()

        if maximizing:

            value = -float('inf')

            for move in state.possible_moves():

                value = max(

                    value,

                    self.alphabeta(
                        state.apply_move(move),
                        alpha,
                        beta,
                        False
                    )
                )

                alpha = max(alpha, value)

                if alpha >= beta:
                    break

            return value

        else:

            value = float('inf')

            for move in state.possible_moves():

                value = min(

                    value,

                    self.alphabeta(
                        state.apply_move(move),
                        alpha,
                        beta,
                        True
                    )
                )

                beta = min(beta, value)

                if alpha >= beta:
                    break

            return value

    def best_move(self, state):

        best_score = -float('inf')
        best_move = None

        for move in state.possible_moves():

            score = self.alphabeta(

                state.apply_move(move),

                -float('inf'),
                float('inf'),

                False
            )

            if score > best_score:

                best_score = score
                best_move = move

        return best_move
state = TicTacToe(

    cells=[
        'X','X','.',
        'O','O','.',
        '.','.','.'
    ],

    turn='X'
)

print("Current Board")
state.display()
alpha_beta = AlphaBetaAgent()
print(
    "Alpha Beta Move:",
    alpha_beta.best_move(state)
)

