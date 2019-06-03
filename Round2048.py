import random

destination_array = {
    "UP": 0,
    "RIGHT": 1,
    "DOWN": 2,
    "LEFT": 3
}


class Round2048:

    def __init__(self):
        self.matrix = [[0] * 4 for i in range(4)]
        self.make_random()
        self.make_random()

        self.score = 0

    def make_random(self):
        rand = random.randint(1, 10)

        if rand <= 9:
            insert_value = 2
        else:
            insert_value = 4

        if not self.check_is_lose():

            all_free_space = []

            for i in range(4):
                for j in range(4):
                    if self.matrix[i][j] == 0:
                        all_free_space.append((i, j))

            random_position = random.choice(all_free_space)
            x = random_position[0]
            y = random_position[1]

            self.matrix[x][y] = insert_value

    def check_is_lose(self):
        for i in range(4):
            for j in range(4):
                if self.matrix[i][j] == 0:
                    return False

        return True

    def pprint(self):
        for i in range(4):
            print(self.matrix[i])
        print()

    def swipe(self, destination):

        # базовый "up", остальные приводимы к нему
        for i in range(destination_array[destination]):
            self._reverse_ccw_matrix()

        # алгоритм слияния -- слили все, что смогли
        for i in range(3):
            for j in range(4):
                if self.matrix[i][j] and (self.matrix[i][j] == self.matrix[i + 1][j]):
                    self.matrix[i][j] += self.matrix[i][j]
                    self.score += self.matrix[i][j]

                    # hardcode
                    if i == 0:
                        self.matrix[1][j] = self.matrix[2][j]
                        self.matrix[2][j] = self.matrix[3][j]
                        self.matrix[3][j] = 0
                    if i == 1:
                        self.matrix[2][j] = self.matrix[3][j]
                        self.matrix[3][j] = 0
                    if i == 2:
                        self.matrix[3][j] = 0

        # алгоритм прижатия к стене
        # не больше 4 раз:
        for i in range(4):
            for k in range(4):
                # hardcode
                if self.matrix[0][k] == 0:
                    self.matrix[0][k] = self.matrix[1][k]
                    self.matrix[1][k] = self.matrix[2][k]
                    self.matrix[2][k] = self.matrix[3][k]
                    self.matrix[3][k] = 0

        for i in range(destination_array[destination]):
            self._reverse_cw_matrix()

    def __str__(self):
        return str(self.matrix)

    def _reverse_ccw_matrix(self):
        self.matrix = [[r[col] for r in self.matrix] for col in range(len(self.matrix[0]))]

    # hardcode
    def _reverse_cw_matrix(self):
        self._reverse_ccw_matrix()
        self._reverse_ccw_matrix()
        self._reverse_ccw_matrix()



if __name__ == "__main__":

    game = Round2048()
    game.pprint()

    game.make_random()
    game.pprint()

