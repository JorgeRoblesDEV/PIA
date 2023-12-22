import random as rand

import os

import configparser


def clear_screen():
    print('\n' * 100)

class MapGrid():
    def __init__(self, ancho = 30, alto = 15, avatar_player = '@', espacios_char = '.', paredes_char = '#', inicio_fin_char = '■'):
        self.inicio_fin_char = inicio_fin_char
        self.mapa = []
        self.paredes = []
        config = configparser.ConfigParser()
        config.read('config.ini')
        config_arr = config['DEFAULT']
        if 'Width' in config_arr:
            self.ancho_mapa = int(config_arr['Width'])
        else:
            self.ancho_mapa = ancho
        if 'Height' in config_arr:
            self.alto_mapa = int(config_arr['Height'])
        else:
            self.alto_mapa = alto
        if 'Avatar' in config_arr:
            self.player = Player(avatar=config_arr['Avatar'])
        else:
            self.player = Player(avatar=avatar_player)
        if 'Spaces' in config_arr:
            if config_arr['Spaces'] == 'ASCII(32)':
                self.espacios_char = ' '
            else:
                self.espacios_char = config_arr['Spaces']
        else:
            self.espacios_char = espacios_char
        if 'Walls' in config_arr:
            self.paredes_char = config_arr['Walls']
        else:
            self.paredes_char = paredes_char
        if 'Start_End' in config_arr:
            self.start_end = config_arr['Start_End']
        else:
            self.start_end = inicio_fin_char
        self.get_grid()
        clear_screen()

        self.get_walls(0.3)
        self.move_player()

    # Crea el mapa de puntos
    def get_grid(self):
        for i in range(self.alto_mapa):
            self.mapa.append([self.espacios_char] * self.ancho_mapa)

        self.mapa[0][0] = self.inicio_fin_char
        self.mapa[-1][-1] = self.inicio_fin_char

    # # Pintar el mapa
    # def draw_grid(self):
    #     for fila in self.mapa:
    #         for elemento in fila:
    #             print(elemento, end=' ')
    #         print()

    # Pintar el mapa con bordes
    def draw_grid(self):
        borde = int(self.ancho_mapa - 6) * "─"

        # Imprimir el encabezado del recuadro
        print("┌" + borde + "DUNGEON-CRAWL" + borde + "┐")

        # Imprimir cada fila del mapa con el recuadro
        for fila in self.mapa:
            print("│ ", end='')
            for elemento in fila:
                print(elemento, end=' ')
            print("│")

        # Imprimir el fondo del recuadro
        print("└───────" + borde + borde + "──────┘", end='', flush=True)

    # Crea las coordenadas de las paredes
    def get_walls(self, pct = 0.3):
        num_paredes = round(self.ancho_mapa * self.alto_mapa * pct // 2)

        for i in range(0, num_paredes):
            coord_x = rand.randint(0, self.ancho_mapa -1)
            coord_y = rand.randint(0, self.alto_mapa -1)
            n_coord = [coord_y, coord_x]

            # Si existe la pared o es la misma que la casilla de finalizar -> Se repite el random
            while n_coord in self.paredes or self.mapa[coord_y][coord_x] == self.mapa[-1][-1]:
                coord_x = rand.randint(0, self.ancho_mapa - 1)
                coord_y = rand.randint(0, self.alto_mapa - 1)
                n_coord = [coord_y, coord_x]

            self.paredes.append(n_coord)

        # Anadir paredes y visualizar
        self.draw_walls()

    # Anadir paredes a mapa y visualizar
    def draw_walls(self):
        # Crear mapa con paredes
        for y in range(self.alto_mapa):
            for x in range(self.ancho_mapa):
                if [y, x] in self.paredes:
                    self.mapa[y][x] = self.paredes_char

        self.draw_player()

    # Dibujar jugador y mostrar mapa
    def draw_player(self):
        # Crear mapa con jugador
        self.modify_player()

        # Visualizar mapa con jugador
        self.draw_grid()

        espacios = int((self.ancho_mapa * 2 - 20) / 2 - 1) * " "
        print("\n" +
              espacios + "┌────MOVIMIENTOS────┐\n" +
              espacios + "│    W     R:Reset  │\n" +
              espacios + "│  A S D   Q:Salir  │\n" +
              espacios + "└───────────────────┘", flush=True)

    def modify_player(self, elemento = None):
        if elemento == None:
            elemento = self.player.avatar
        for y in range(self.alto_mapa):
            for x in range(self.ancho_mapa):
                if x == self.player.coor_x and y == self.player.coor_y:
                    self.mapa[y][x] = elemento
                    if self.player.coor_x == 0 and self.player.coor_y == 0:
                        self.mapa[y][x] = self.inicio_fin_char

    def move_player(self):
        # Windows
        if os.name == 'nt':
            from Move_payer_windows import move_player
            move_player(self)
        # Linux
        elif os.name == 'posix':
            from Move_player_linux import move_player
            move_player(self)
        else:
            print("Sistema operativo no compatible")

    def move_player_previous(self):
        self.modify_player(elemento=self.espacios_char)

    def play_again(self):
        while True:
            response = input("\n¿Quieres jugar otra partida? (s/n): ").lower()
            if response == 's':
                return True
            elif response == 'n':
                return False
            else:
                print("Por favor, introduce 's' para sí o 'n' para no.")

    def reset_game(self):
        # Limpiar los arrays

        self.mapa = []
        self.paredes = []

        # Reiniciar las posiciones del jugador y recrear el mapa
        self.player.coor_x = 0
        self.player.coor_y = 0
        self.get_grid()

        clear_screen()
        # Volver a crear las paredes
        self.get_walls(0.3)
        self.move_player()


class Player():
    def __init__(self, avatar = 'P'):
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

        # Verificar limites del mapa
        if 0 <= new_x < len(mapa[0]) and 0 <= new_y < len(mapa):
            # Si no es una pared
            if mapa[new_y][new_x] != '#':
                self.coor_x, self.coor_y = new_x, new_y

        return self.coor_x, self.coor_y





