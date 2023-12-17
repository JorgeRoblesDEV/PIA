import random
import os
import time

class GameOfLife:
    DEFAULT_CELL_WIDTH = 10
    DEFAULT_CELL_HEIGHT = 10
    DEFAULT_INIT_ALIVE_CELLS_NUM = 20
    DEFAULT_GAME_TURNS = 10
    DEFAULT_SLEEP_TIME = 0.25
    ALIVE = '*'
    DEAD = '.'

    def __init__(self, width=None, height=None, init_alive_cells_num=None, game_turns=None, sleep_time=None):
        self.width = width or self.DEFAULT_CELL_WIDTH
        self.height = height or self.DEFAULT_CELL_HEIGHT
        self.init_alive_cells_num = init_alive_cells_num or self.DEFAULT_INIT_ALIVE_CELLS_NUM
        self.game_turns = game_turns or self.DEFAULT_GAME_TURNS
        self.sleep_time = sleep_time or self.DEFAULT_SLEEP_TIME
        self.grid = []
        self.llenar_con_celdas_muertas()
        self.set_init_alive_cells()

    def clear(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def wait(self):
        time.sleep(self.sleep_time)

    def llenar_con_celdas_muertas(self):
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(self.DEAD)
            self.grid.append(row)

    def draw_grid(self):
        for row in self.grid:
            for cell in row:
                print(cell, end=' ')
            print()
        print()

    def set_init_alive_cells(self):
        i = 0
        while i < self.init_alive_cells_num:
            while True:
                x, y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
                if self.grid[y][x] == self.DEAD:
                    self.grid[y][x] = self.ALIVE
                    break
            i += 1

    def get_cell_living_neighbors(self, x, y):
        living_neighbors = 0
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height and self.grid[ny][nx] == self.ALIVE:
                    living_neighbors += 1
        return living_neighbors

    def next_turn_grid(self):
        next_grid = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(self.DEAD)
            next_grid.append(row)

        for y in range(self.height):
            for x in range(self.width):
                living_neighbors = self.get_cell_living_neighbors(x, y)
                if self.grid[y][x] == self.ALIVE:
                    if living_neighbors < 2 or living_neighbors > 3:
                        next_grid[y][x] = self.DEAD
                    else:
                        next_grid[y][x] = self.ALIVE
                elif living_neighbors == 3:
                    next_grid[y][x] = self.ALIVE

        self.grid = next_grid

    def init_game(self):
        self.set_init_alive_cells()

        turn = 1
        while turn <= self.game_turns:
            self.clear()
            print('Turno:' + str(turn))
            self.draw_grid()
            self.next_turn_grid()
            self.wait()
            turn += 1
