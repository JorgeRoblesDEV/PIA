import random as rn
import numpy as np

from Game import Game


class TicTacToe(Game):
    def __init__(self):
        super().__init__()
        self.tablero = None
        self.current_player = None
        self.players = [' ', 'O', 'X']
        self.game_reset()

    def print_tablero(self, tablero):
        print("+---+---+---+")
        print("| " + str(self.players[tablero[0][0]]) + " | " + str(self.players[tablero[0][1]]) + " | " + str(
            self.players[tablero[0][2]]) + " |")
        print("+---+---+---+")
        print("| " + str(self.players[tablero[1][0]]) + " | " + str(self.players[tablero[1][1]]) + " | " + str(
            self.players[tablero[1][2]]) + " |")
        print("+---+---+---+")
        print("| " + str(self.players[tablero[2][0]]) + " | " + str(self.players[tablero[2][1]]) + " | " + str(
            self.players[tablero[2][2]]) + " |")
        print("+---+---+---+")

    def instructions(self):
        print("Instructions:")
        print("Las celdas del tablero están basadas en el teclado numérico.\n"
              "Para seleccionar una celda se debe teclear el número y aceptarlo con Enter.\n")
        print("+---+---+---+")
        print("| 7 | 8 | 9 |")
        print("| 4 | 5 | 6 |")
        print("| 1 | 2 | 3 |")
        print("+---+---+---+\n")

    def numeric_2_position(self, numeric):
        if numeric == 7:
            return 0, 0
        elif numeric == 8:
            return 0, 1
        elif numeric == 9:
            return 0, 2
        elif numeric == 4:
            return 1, 0
        elif numeric == 5:
            return 1, 1
        elif numeric == 6:
            return 1, 2
        elif numeric == 1:
            return 2, 0
        elif numeric == 2:
            return 2, 1
        elif numeric == 3:
            return 2, 2
        else:
            return -1, -1

    def is_full(self, tablero):
        full = True
        for i in range(0, len(tablero)):
            for j in range(len(tablero[i])):
                if tablero[i][j] == 0:
                    full = False
        return full

    def check_arr(self, array):
        eq = False
        val = array[0]
        for i in range(len(array)):
            if val != array[i]:
                break
        else:
            if val != 0:
                eq = True
        return eq

    def check_rows(self, tablero):
        eq = False
        for i in range(len(tablero)):
            eq = self.check_arr(tablero[i])
            if eq:
                break
        return eq

    def check_cols(self, tablero):
        eq = False
        for i in range(len(tablero[0])):
            eq = self.check_arr([row[i] for row in tablero])
            if eq:
                break
        return eq

    def check_diags(self, tablero):
        eq = False
        l = len(tablero)
        if self.check_arr([tablero[i][i] for i in range(l)]):
            eq = True
        elif self.check_arr([tablero[l - 1 - i][i] for i in range(l - 1, -1, -1)]):
            eq = True
        return eq

    def has_won(self, tablero):
        won = False
        if self.check_rows(tablero):
            won = True
        elif self.check_cols(tablero):
            won = True
        elif self.check_diags(tablero):
            won = True
        return won

    def output_title(self):
        print("")
        print("###############################")
        print("######### TIC TAC TOE #########")
        print("###############################")
        print("")

    def game_init(self, config):
        self.clear_screen()
        self.output_title()
        self.instructions()
        self.game_reset()

        while not self.game_is_finish():
            self.game_print()
            in_str = self.game_input()
            self.game_turn(in_str)

        print(self.game_finish_msg())
        self.game_print()
        seguir = input("¿Otra partida? [Y/n]").upper()
        while seguir not in ['Y', 'N']:
            print("Ingresa una opción válida.")
            seguir = input("¿Otra partida? [Y/n]").upper()
        if seguir == 'Y':
            self.game_reset()

    def game_input(self) -> str:
        while True:
            char = input("Introduce posición, jugador " + self.players[self.current_player] + "\n")

            if not char:
                self.game_print()
                print("Por favor, ingresa una posición válida.")
                continue

            try:
                fil, col = self.numeric_2_position(int(char))
            except ValueError:
                self.game_print()
                print("Valor inadecuado. Por favor, ingresa un número válido.")
                continue

            if (fil == -1) or (col == -1):
                self.game_print()
                print("Valor inadecuado")
                continue

            if self.tablero[fil][col] != 0:
                self.game_print()
                print("Valor ya introducido")
                continue

            break

        return char

    def game_turn(self, in_str):
        if in_str.isdigit():
            fil, col = self.numeric_2_position(int(in_str))
            if (fil != -1) and (col != -1) and self.tablero[fil][col] == 0:
                self.tablero[fil][col] = self.current_player
                self.current_player *= -1

    def game_print(self):
        self.clear_screen()
        self.output_title()
        self.instructions()

        self.print_tablero(self.tablero)

    def game_is_finish(self) -> bool:
        if self.has_won(self.tablero):
            print("El jugador ", self.players[self.current_player * -1], " ha ganado")
            return True
        elif self.is_full(self.tablero):
            print("EMPATE")
            return True
        return False

    def game_finish_msg(self) -> str:
        return "Partida finalizada"

    def game_reset(self):
        self.current_player = 1
        self.tablero = np.zeros((3, 3), dtype=int)
        self.clear_and_print_board()

    def clear_and_print_board(self):
        self.clear_screen()
        self.output_title()
        self.instructions()
        self.print_tablero(self.tablero)

def main_tictac():
    TicTacToe().game_init(None)
