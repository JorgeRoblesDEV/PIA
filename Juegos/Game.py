class Game:
    def __init__(self):
        pass

    def menu(self):
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
                    main_dungeon()
                elif opt == "3":
                    from Conway import main_conway
                    main_conway()
                elif opt == "4":
                    print("\nGracias por entretenerte con nosotros. ¡Hasta luego!")
                    break;
                else:
                    print("El juego seleccionado no existe.")
        except EOFError:
            self.menu()
        except KeyboardInterrupt:
            self.menu()

    def game_init(self, config):
        pass

    def game_input(self) -> str:
        pass

    def game_turn(self, in_str):
        pass

    def game_print(self):
        pass

    def game_is_finish(self) -> bool:
        pass

    def game_finish_msg(self) -> str:
        pass

    def clear_screen(self):
        print('\n' * 100)
