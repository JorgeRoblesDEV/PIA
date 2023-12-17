from Conway import GameOfLife

if __name__ == "__main__":
    game = GameOfLife(width=30, height=30, init_alive_cells_num=60, sleep_time=0.25, game_turns=20)
    game.init_game()
