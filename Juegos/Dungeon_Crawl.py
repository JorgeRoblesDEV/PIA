import random as rand
import os
from Game import Game


class MapGrid(Game):
    def __init__(self, ancho=30, alto=15, avatar_player='@', espacios_char='.', paredes_char='#', inicio_fin_char='■'):
        super().__init__()

        self.inicio_fin_char = inicio_fin_char
        self.mapa = []
        self.paredes = []

        self.player = Player(avatar=avatar_player)
        self.espacios_char = espacios_char
        self.paredes_char = paredes_char
        self.start_end = inicio_fin_char
        self.ancho_mapa = ancho
        self.alto_mapa = alto

    def get_grid(self):
        for i in range(self.alto_mapa):
            self.mapa.append([self.espacios_char] * self.ancho_mapa)
        self.mapa[0][0] = self.inicio_fin_char
        self.mapa[-1][-1] = self.inicio_fin_char

    def draw_grid(self):
        borde = int(self.ancho_mapa - 6) * "─"

        print("┌" + borde + "DUNGEON-CRAWL" + borde + "┐")

        for fila in self.mapa:
            print("│ ", end='')
            for elemento in fila:
                print(elemento, end=' ')
            print("│")

        print("└───────" + borde + borde + "──────┘", end='', flush=True)

    def get_walls(self, pct=0.3):
        num_paredes = round(self.ancho_mapa * self.alto_mapa * pct // 2)

        for i in range(0, num_paredes):
            coord_x = rand.randint(0, self.ancho_mapa - 1)
            coord_y = rand.randint(0, self.alto_mapa - 1)
            n_coord = [coord_y, coord_x]

            while n_coord in self.paredes or self.mapa[coord_y][coord_x] == self.mapa[-1][-1]:
                coord_x = rand.randint(0, self.ancho_mapa - 1)
                coord_y = rand.randint(0, self.alto_mapa - 1)
                n_coord = [coord_y, coord_x]

            self.paredes.append(n_coord)

        self.draw_walls()

    def draw_walls(self):
        for y in range(self.alto_mapa):
            for x in range(self.ancho_mapa):
                if [y, x] in self.paredes:
                    self.mapa[y][x] = self.paredes_char

        self.draw_player()

    def draw_player(self):
        self.modify_player()
        self.draw_grid()

        espacios = int((self.ancho_mapa * 2 - 20) / 2 - 1) * " "
        print("\n" +
              espacios + "┌────MOVIMIENTOS────┐\n" +
              espacios + "│    W     R:Reset  │\n" +
              espacios + "│  A S D   Q:Salir  │\n" +
              espacios + "└───────────────────┘", flush=True)

    def modify_player(self, elemento=None):
        if elemento is None:
            elemento = self.player.avatar
        for y in range(self.alto_mapa):
            for x in range(self.ancho_mapa):
                if x == self.player.coor_x and y == self.player.coor_y:
                    self.mapa[y][x] = elemento
                    if self.player.coor_x == 0 and self.player.coor_y == 0:
                        self.mapa[y][x] = self.inicio_fin_char

    def move_player(self):
        if os.name == 'nt':
            from Move_payer_windows import move_player
            move_player(self)
        elif os.name == 'posix':
            from ove_player_linux import move_player
            move_player(self)
        else:
            print("Sistema operativo no compatible")

    def move_player_previous(self):
        self.modify_player(elemento=self.espacios_char)

    def game_init(self, config):
        if 'Width' in config:
            self.ancho_mapa = int(config['Width'])
        if 'Height' in config:
            self.alto_mapa = int(config['Height'])
        if 'Avatar' in config:
            self.player = Player(avatar=config['Avatar'])
        if 'Spaces' in config:
            if config['Spaces'] == 'ASCII(32)':
                self.espacios_char = ' '
            else:
                self.espacios_char = config['Spaces']
        if 'Walls' in config:
            self.paredes_char = config['Walls']
        if 'Start_End' in config:
            self.start_end = config['Start_End']

        while True:
            self.clear_screen()
            self.game_reset()

            while not self.game_is_finish():
                self.game_print()
                in_str = self.game_input()
                self.game_turn(in_str)

            print(self.game_finish_msg())
            self.game_print()

            if not self.play_again():
                break

    def game_input(self) -> str:
        while True:
            char = input("\nIntroduce movimiento (W/A/S/D), Q para salir, R para reiniciar:\n").lower()

            if char not in ['w', 'a', 's', 'd', 'q', 'r']:
                self.game_print()
                print("Movimiento no válido. Por favor, ingresa un movimiento válido.")
                continue

            break

        return char

    def game_turn(self, in_str):
        if in_str == 'q':
            print("Saliendo del juego.")
            exit()
        elif in_str == 'r':
            print("Reiniciando el juego.")
            self.game_reset()
        else:
            self.player.move(in_str, self.mapa)

    def game_print(self):
        self.clear_screen()
        self.draw_grid()

    def game_is_finish(self) -> bool:
        return self.player.coor_x == self.ancho_mapa - 1 and self.player.coor_y == self.alto_mapa - 1

    def game_finish_msg(self) -> str:
        return "Partida finalizada"

    def game_reset(self):
        self.clear_screen()

        self.mapa = []
        self.paredes = []
        self.player.coor_x = 0
        self.player.coor_y = 0
        self.get_grid()
        self.get_walls(0.3)
        self.move_player()

    def clear_and_print_board(self):
        self.clear_screen()
        self.draw_grid()

    def play_again(self):
        while True:
            response = input("\n¿Quieres jugar otra partida? (s/n): ").lower()
            if response == 's':
                return True
            elif response == 'n':
                print("Saliendo del juego.")
                break
            else:
                print("Por favor, introduce 's' para sí o 'n' para no.")


class Player():
    def __init__(self, avatar='P'):
        self.avatar = avatar
        self.coor_x = 0
        self.coor_y = 0

    def move(self, typed, mapa):
        new_x, new_y = self.coor_x, self.coor_y

        if typed == 'w':
            new_y = self.coor_y - 1
        elif typed == 'a':
            new_x = self.coor_x - 1
        elif typed == 's':
            new_y = self.coor_y + 1
        elif typed == 'd':
            new_x = self.coor_x + 1

        if 0 <= new_x < len(mapa[0]) and 0 <= new_y < len(mapa):
            if mapa[new_y][new_x] != '#':
                self.coor_x, self.coor_y = new_x, new_y

        return self.coor_x, self.coor_y


def main_dungeon(configParser):
    MapGrid().game_init(configParser['DUNGEON'])