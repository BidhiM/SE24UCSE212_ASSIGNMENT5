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
class HeuristicAlphaBetaAgent:

    def evaluate(self, state):

        lines = [

            [0,1,2],
            [3,4,5],
            [6,7,8],

            [0,3,6],
            [1,4,7],
            [2,5,8],

            [0,4,8],
            [2,4,6]
        ]

        score = 0

        for line in lines:

            values = [state.cells[i] for i in line]

            if values.count('X') == 2 and values.count('.') == 1:
                score += 10

            if values.count('O') == 2 and values.count('.') == 1:
                score -= 10

            if values.count('X') == 1 and values.count('.') == 2:
                score += 1

            if values.count('O') == 1 and values.count('.') == 2:
                score -= 1

        return score

    def search(
        self,
        state,
        depth,
        alpha,
        beta,
        maximizing
    ):

        if state.game_over():
            return state.score() * 100

        if depth == 0:
            return self.evaluate(state)

        if maximizing:

            value = -float('inf')

            for move in state.possible_moves():

                value = max(

                    value,

                    self.search(
                        state.apply_move(move),
                        depth - 1,
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

                    self.search(
                        state.apply_move(move),
                        depth - 1,
                        alpha,
                        beta,
                        True
                    )
                )

                beta = min(beta, value)

                if alpha >= beta:
                    break

            return value

    def best_move(self, state, depth=4):

        best_score = -float('inf')
        selected = None

        for move in state.possible_moves():

            score = self.search(

                state.apply_move(move),

                depth,

                -float('inf'),
                float('inf'),

                False
            )

            if score > best_score:

                best_score = score
                selected = move

        return selected
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
heuristic = HeuristicAlphaBetaAgent()
print(
    "Heuristic Move:",
    heuristic.best_move(state)
)
