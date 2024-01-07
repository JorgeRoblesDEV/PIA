import random as rn
import numpy as np
import os

from Game import Game


class TicTacToe(Game):
    def __init__(self):
        super().__init__()
        self.players = [' ', 'O', 'X']

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

    def clear_display(self):
        if os.name == 'posix':
            os.system('clear')
        elif os.name == 'nt':  # Windows
            os.system('cls')

    def game(self):
        seguir = True

        while seguir:
            self.clear_display()
            self.output_title()

            self.instructions()

            first_player_idx = 1 if rn.randint(0, 1) == 0 else -1
            second_player_idx = 1 if first_player_idx == -1 else -1
            print("First player: ", str(self.players[first_player_idx]))
            print("Second player: ", str(self.players[second_player_idx]))

            tablero = np.zeros((3, 3), dtype=int)
            self.print_tablero(tablero)

            current_player = first_player_idx

            while not self.is_full(tablero):
                in_ok = False
                scape = False
                fil = -1
                col = -1

                while not in_ok:
                    char = input("Introduce posición, jugador " + self.players[current_player] + "\n")

                    self.clear_display()
                    self.output_title()

                    if not char:
                        self.print_tablero(tablero)
                        print("Por favor, ingresa una posición válida.")
                        continue

                    if char == 'C':
                        print("Partida terminada por caracter de escape")
                        scape = True
                        break

                    try:
                        fil, col = self.numeric_2_position(int(char))
                    except ValueError:
                        self.print_tablero(tablero)
                        print("Valor inadecuado. Por favor, ingresa un número válido.")
                        continue

                    if (fil == -1) & (col == -1):
                        self.print_tablero(tablero)
                        print("Valor inadecuado")
                        continue

                    if tablero[fil][col] != 0:
                        self.print_tablero(tablero)
                        print("Valor ya introducido")
                        continue

                    in_ok = True

                if scape:
                    break

                tablero[fil][col] = current_player
                self.print_tablero(tablero)

                if self.has_won(tablero):
                    print("El jugador ", self.players[current_player], " ha ganado")
                    seguir = True if input("Otra partida? [Y/n]").upper() == 'Y' else False
                    break

                current_player = current_player * -1
            else:
                print("EMPATE")
                seguir = True if input("Otra partida? [Y/n]").upper() == 'Y' else False


def main_tictac():
    TicTacToe().game()
