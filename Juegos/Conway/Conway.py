import random
import os
import time

import configparser

class GameOfLife():
    DEFAULT_CELL_WIDTH = 10
    DEFAULT_CELL_HEIGHT = 10
    DEFAULT_INIT_ALIVE_CELLS_NUM = 20
    DEFAULT_GAME_TURNS = 10
    DEFAULT_SLEEP_TIME = 0.25
    ALIVE = '*'
    DEAD = '.'

    def __init__(self, width=None, height=None, init_alive_cells_num=None, game_turns=None, sleep_time=None):
        config = configparser.ConfigParser()
        config.read('config.ini')
        config_arr = config['DEFAULT']
        if 'Width' in config_arr:
            self.width = int(config_arr['Width'])
        else:
            self.width = width or self.DEFAULT_CELL_WIDTH
        if 'Height' in config_arr:
            self.height = int(config_arr['Height'])
        else:
            self.height = height or self.DEFAULT_CELL_HEIGHT
        if 'Init_alive_cells_num' in config_arr:
            self.init_alive_cells_num = int(config_arr['Init_alive_cells_num'])
        else:
            self.init_alive_cells_num = init_alive_cells_num or self.DEFAULT_INIT_ALIVE_CELLS_NUM
        if 'Game_turns' in config_arr:
            self.game_turns = int(config_arr['Game_turns'])
        else:
            self.game_turns = game_turns or self.DEFAULT_GAME_TURNS

        if 'Sleep_time' in config_arr:
            self.sleep_time = float(config_arr['Sleep_time'])
        else:
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
            fila = []
            for j in range(self.width):
                fila.append(self.DEAD)
            self.grid.append(fila)

    def draw_grid(self):
        for fila in self.grid:
            for elemento in fila:
                print(elemento, end=' ')
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

    def get_cell_living_neighbors(self, x_celda, y_celda):
        cantidad_vecinos_vivos = 0
        for desplazamiento_y in [-1, 0, 1]:
            for desplazamiento_x in [-1, 0, 1]:
                if desplazamiento_x == 0 and desplazamiento_y == 0:
                    continue
                x_vecino, y_vecino = x_celda + desplazamiento_x, y_celda + desplazamiento_y
                if 0 <= x_vecino < self.width and 0 <= y_vecino < self.height and self.grid[y_vecino][
                    x_vecino] == self.ALIVE:
                    cantidad_vecinos_vivos += 1

        return cantidad_vecinos_vivos

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

        turno = 1
        while turno <= self.game_turns:
            self.clear()
            print('Turno:' + str(turno))
            self.draw_grid()
            self.next_turn_grid()
            self.wait()
            turno += 1
