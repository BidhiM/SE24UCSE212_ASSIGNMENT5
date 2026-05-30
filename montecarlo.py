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
class MCTSNode:

    def __init__(
        self,
        state,
        parent=None,
        move=None
    ):

        self.state = state
        self.parent = parent
        self.move = move

        self.children = []

        self.visits = 0
        self.wins = 0

        self.untried_moves = state.possible_moves()

    def ucb1(self, exploration=1.41):

        if self.visits == 0:
            return float('inf')

        return (

            self.wins / self.visits +

            exploration *

            math.sqrt(
                math.log(self.parent.visits) / self.visits
            )
        )


class MCTSAgent:

    def select(self, node):

        while not node.state.game_over():

            if node.untried_moves:
                return self.expand(node)

            node = max(
                node.children,
                key=lambda child: child.ucb1()
            )

        return node

    def expand(self, node):

        move = random.choice(node.untried_moves)

        node.untried_moves.remove(move)

        child_state = node.state.apply_move(move)

        child_node = MCTSNode(
            child_state,
            node,
            move
        )

        node.children.append(child_node)

        return child_node

    def simulate(self, state):

        current = deepcopy(state)

        while not current.game_over():

            move = random.choice(
                current.possible_moves()
            )

            current = current.apply_move(move)

        return current.score()

    def backpropagate(self, node, result):

        while node:

            node.visits += 1
            node.wins += result

            node = node.parent

    def best_move(self, state, iterations=1000):

        root = MCTSNode(state)

        for _ in range(iterations):

            node = self.select(root)

            result = self.simulate(node.state)

            self.backpropagate(node, result)

        best_child = max(
            root.children,
            key=lambda child: child.visits
        )

        return best_child.move
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
mcts = MCTSAgent()
print(
    "MCTS Move:",
    mcts.best_move(state, 2000)
)


