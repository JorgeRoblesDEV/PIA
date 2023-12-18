import TIC_TAC_TOE.Main as tic
import Dungeon_Crawl.Main as dc
import Conway.Main as con
class Juegos():
    def __init__(self):
        abc = 3

    def menu(self):
        print("\n" +
              "┌───────GAMES───────┐\n" +
              "│  1. TIC TAC TOE   │\n" +
              "│  2. DUNGEON CRAWL │\n" +
              "│  3. CONWAY        │\n" +
              "└───────────────────┘\n\n", flush=True)

        opt = int(input("Seleccionar juego: "))

        if opt == 1:
            tic.main()
        elif opt == 2:
            dc.main()
        elif opt == 3:
            con.main()
        else:
            print("El juego seleccionado no existe.")
