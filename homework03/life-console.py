import curses


from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """ Отобразить рамку. """
        screen.clear()
        height, width = screen.getmaxyx()
        string = ""
        for row in range(height):
            for col in range(width):
                if row == 0 or row == (height - 1):
                    if col == 0 or col == width:
                        string += "+"
                    else:
                        string += "-"
                elif row < (height - 1) and row > 0:
                    if col == 0 or col == (width - 1):
                        string += "|"
                    else:
                        string += " "
            try:
                screen.addstr(string)
            except curses.error:
                pass
            string = ""

        self.draw_grid(screen)

        screen.refresh()
        screen.getch()

    def draw_grid(self, screen) -> None:
        """ Отобразить состояние клеток. """
        height, width = screen.getmaxyx()

        x = (width - self.life.cols) // 2
        y = (height - self.life.rows) // 2

        for сount_row, just_row in enumerate(self.life.curr_generation):
            for count_col, just_col in enumerate(just_row):
                if just_col:
                    try:
                        screen.addstr(count_row + y, count_col + x, "*")
                    except curses.error:
                        pass

    def run(self) -> None:
        screen = curses.initscr()
        curses.wrapper(self.draw_borders)
        while self.life.is_max_generations_exceeded and not self.life.is_changing:
            self.life.step()
            self.draw_borders(screen)
        curses.endwin()


if __name__ == "__main__":
    life = GameOfLife((24, 80), max_generations=50)
    gui = Console(life)
    gui.run()
