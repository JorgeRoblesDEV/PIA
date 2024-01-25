import random
import os
import time
from Game import Game

class GameOfLife(Game):
    DEFAULT_CELL_WIDTH = 10
    DEFAULT_CELL_HEIGHT = 10
    DEFAULT_INIT_ALIVE_CELLS_NUM = 20
    DEFAULT_GAME_TURNS = 10
    ALIVE = '*'
    DEAD = '.'

    def __init__(self):
        super().__init__()

        self.grid = []
        self.current_turn = 1

    def clear(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

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

    def game_init(self, config):
        self.config = config
        if 'Width' in self.config:
            self.width = int(self.config['Width'])
        else:
            self.width = self.DEFAULT_CELL_WIDTH
        if 'Height' in self.config:
            self.height = int(self.config['Height'])
        else:
            self.height = self.DEFAULT_CELL_HEIGHT
        if 'Init_alive_cells_num' in self.config:
            self.init_alive_cells_num = int(self.config['Init_alive_cells_num'])
        else:
            self.init_alive_cells_num = self.DEFAULT_INIT_ALIVE_CELLS_NUM
        if 'Game_turns' in self.config:
            self.game_turns = int(self.config['Game_turns'])
        else:
            self.game_turns = self.DEFAULT_GAME_TURNS

        self.llenar_con_celdas_muertas()
        self.set_init_alive_cells()

        while not self.game_is_finish():
            self.game_print()
            in_str = self.game_input()
            self.game_turn(in_str)

    def game_input(self) -> str:
        return input("Enter para avanzar al siguiente turno (o 'q' para salir): ").lower()

    def game_turn(self, in_str):
        if in_str == 'q':
            print("Saliendo del juego.")
            self.game_finish_msg()
            exit()

        self.clear()
        print(f'Turno actual: {self.current_turn}')
        self.draw_grid()
        self.next_turn_grid()
        self.current_turn += 1

    def game_print(self):
        self.clear()
        print(f'Turno actual: {self.current_turn}')
        self.draw_grid()

    def game_reset(self):
        self.clear()
        self.grid = []
        self.current_turn = 1
        self.llenar_con_celdas_muertas()
        self.set_init_alive_cells()

    def game_is_finish(self) -> bool:
        return self.current_turn > self.game_turns

    def game_finish_msg(self) -> str:
        return "Juego finalizado."

def main_conway(configParser):
    GameOfLife().game_init(configParser['CONWAY'])

if __name__ == "__main__":
    main_conway()
