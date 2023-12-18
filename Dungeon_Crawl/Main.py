from Dungeon_Crawl import MapGrid

def main():
    dang = MapGrid(30,15)
    dang.get_walls(0.3)
    dang.move_player()

if __name__ == "__main__":
    main()