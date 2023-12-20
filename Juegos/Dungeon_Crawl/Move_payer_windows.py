from Dungeon_Crawl import clear_screen

import msvcrt
import sys

def move_player(self):
    while True:
        try:
            if msvcrt.kbhit():
                movement = msvcrt.getch().decode().lower()
                if movement == 'q':
                    print("\n\nGracias por haber jugado a Dungeon Crawl. Vuelve pronto.")
                    sys.exit()
                elif movement == 'r':
                    # Reiniciar el juego
                    self.reset_game()
                else:
                    clear_screen()
                    # Poner '.' a la ubicación del jugador antes de mover
                    self.move_player_previous()
                    # Mover jugador
                    self.player.coor_x, self.player.coor_y = self.player.move(movement, self.mapa)
                    self.draw_player()

                    # Verificar si el jugador ha ganado
                    if self.player.coor_x == self.ancho_mapa - 1 and self.player.coor_y == self.alto_mapa - 1:
                        print("\n\n¡Felicidades! Has ganado la partida.")
                        # Preguntar si desea jugar otra partida
                        if self.play_again():
                            # Reiniciar el juego
                            self.reset_game()
                        else:
                            sys.exit()
        # La excepción salta cuando se introduce un caracter No utf-8
        except UnicodeDecodeError:
            print("", end="")