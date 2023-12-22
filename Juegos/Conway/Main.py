from Juegos.Conway.Conway import GameOfLife

def main():
    game = GameOfLife(width=30, height=30, init_alive_cells_num=60, sleep_time=0.25, game_turns=20)
    game.init_game()

if __name__ == "__main__":
    main()