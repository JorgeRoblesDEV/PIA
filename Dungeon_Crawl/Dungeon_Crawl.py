import random as rand

import os


def clear_screen():
    print('\n' * 100)

class MapGrid():
    def __init__(self, ancho = 30, alto = 15):
        clear_screen()

        self.ancho_mapa = ancho
        self.alto_mapa = alto
        self.player = Player(avatar='@')
        self.mapa = []
        self.paredes = []
        self.get_grid()

    # Crea el mapa de puntos
    def get_grid(self):
        for i in range(self.alto_mapa):
            self.mapa.append(['.'] * self.ancho_mapa)

        self.mapa[0][0] = '■'
        self.mapa[-1][-1] = '■'

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
                    self.mapa[y][x] = '#'

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
                        self.mapa[y][x] = '■'

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
        self.modify_player(elemento='.')

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





