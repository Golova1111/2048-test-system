# ================================================
import random
from pprint import pprint

from Round2048 import Round2048


def my_algorithm(matrix):
    return random.choice(["LEFT", "RIGHT", "UP", "DOWN"])


all_algorithms = \
    {
        "Holovashchenko": my_algorithm
    }

# ================================================

COUNT_OF_START = 5

# ================================================

def check_algorithm(function):

    max_score = 0
    max_swipe = 0

    for i in range(COUNT_OF_START):
        game = Round2048()
        swipe = 0

        print("Test iteration", i + 1, "...")
        while not game.check_is_lose():
            answer = function(game.matrix)
            game.swipe(answer)
            game.make_random()
            swipe += 1

        print("Count of swipe:", swipe)
        print("Score:", game.score)
        print()

        if swipe > max_swipe:
            max_swipe = swipe
        if game.score > max_score:
            max_score = game.score

    print("Max score:", max_score)
    return max_score


def main():

    result = {}

    for name, function in all_algorithms.items():
        print("======== Test algorithm:", name)
        score = check_algorithm(function)
        result[name] = score

    result_tuple = sorted(result.items(), key=lambda x: x[1])
    pprint(result_tuple)


if __name__ == "__main__":
    main()