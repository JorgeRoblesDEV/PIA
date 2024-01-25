import sys
import tty
import termios


def move_player(self):
    while True:
        try:
            movement = getch(self).lower()

            if movement == 'q':
                print("\n\nGracias por haber jugado a Dungeon Crawl. Vuelve pronto.")
                sys.exit()
            elif movement == 'r':
                # Reiniciar el juego
                self.game_reset()
            else:
                self.clear_screen()
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
                        self.game_reset()
                    else:
                        sys.exit()

        except UnicodeDecodeError:
            print("", end="")


# LINUX
def getch(self):
    # Lee una sola tecla sin necesidad de presionar Enter
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        char = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return char
