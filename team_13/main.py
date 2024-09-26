import random
from pprint import pprint
from speaker import Caller

# Move/Key - Units moved
MOVES = {
    "F": (0, 1),
    "B": (0, -1),
    "L": (1, 0),
    "R": (-1, 0),
    # "ROT": 0,
    # "CLAP": 0,
}


def add_delta_to_move(orig, delta):
    ox, oy = orig
    dx, dy = delta
    return (ox + dx), (oy + dy)


def return_to_zero(current_pos):
    x, y = current_pos
    if x > 0:
        dx = ["R"] * abs(x)
    elif x < 0:
        dx = ["L"] * abs(x)
    else:
        dx = []

    if y > 0:
        dy = ["B"] * abs(y)
    elif y < 0:
        dy = ["F"] * abs(y)
    else:
        dy = []

    moves = []
    moves.extend(dx)
    moves.extend(dy)
    print(current_pos, x, y)
    print(dx)
    print(dy)
    print(moves)

    return moves


def generate_dance():
    dance = []
    moves = list(MOVES.keys())
    pos = (0, 0)
    for i in range(10):
        move = random.choice(moves)
        delta = MOVES[move]
        pos = add_delta_to_move(pos, delta)
        dance.append(random.choice(moves))
    return_moves = return_to_zero(pos)
    dance.extend(return_moves)
    return dance


if __name__ == "__main__":
    dance = generate_dance()

    pos = (0, 0)
    for i, move in enumerate(dance):
        delta = MOVES[move]
        pos = add_delta_to_move(pos, delta)
        print(f"{i:>2}: {move} {pos}")

    Caller().call(dance)
