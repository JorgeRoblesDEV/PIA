from Dungeon_Crawl import MapGrid

# SE EJECUTA DESDE TERMINAL DE LINUX
if __name__ == "__main__":
    dang = MapGrid(30,15)
    dang.get_walls(0.3)
    dang.move_player()
