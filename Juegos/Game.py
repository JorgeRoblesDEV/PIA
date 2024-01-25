import os
import configparser

class Game:
    def __init__(self):
        self.configParser = configparser.ConfigParser()
        self.configParser.read('config.ini')

    def menu(self):
        self.clear_screen()
        try:
            while True:
                print("\n" +
                      "┌───────GAMES───────┐\n" +
                      "│  1. TIC TAC TOE   │\n" +
                      "│  2. DUNGEON CRAWL │\n" +
                      "│  3. CONWAY        │\n" +
                      "│  4. Exit          │\n" +
                      "└───────────────────┘\n\n", flush=True)

                opt = str(input("Seleccionar juego: "))

                if opt == "1":
                    from Tic_tac_toe import main_tictac
                    main_tictac()
                elif opt == "2":
                    from Dungeon_Crawl import main_dungeon
                    main_dungeon(self.configParser)
                elif opt == "3":
                    from Conway import main_conway
                    main_conway(self.configParser)
                elif opt == "4":
                    print("\nGracias por entretenerte con nosotros. ¡Hasta luego!")
                    break;
                else:
                    self.clear_screen()
                    print("El juego seleccionado no existe.")
        except EOFError:
            self.menu()
        except KeyboardInterrupt:
            self.menu()

    def clear_screen(self):
        if os.name == 'posix':
            os.system('clear')
        elif os.name == 'nt':  # Windows
            os.system('cls')

    def game_init(self, config):
        pass

    def game_input(self) -> str:
        pass

    def game_turn(self, in_str):
        pass

    def game_print(self):
        pass

    def game_reset(self):
        pass

    def game_is_finish(self) -> bool:
        pass

    def game_finish_msg(self) -> str:
        pass
