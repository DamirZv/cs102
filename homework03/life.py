import pathlib
import random

import typing as tp
from copy import deepcopy


Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        # Copy from previous assignment
        grid = []
        if randomize == False:
            grid = [[0 for j in range(self.cols)] for i in range(self.rows)]
        else:
            grid = [[random.randint(0, 1) for j in range(self.cols)] for i in range(self.rows)]
        return grid

    def get_neighbours(self, cell: Cell) -> Cells:
        # Copy from previous assignment
        neighbours = []
        row, col = cell
        for i in range(max(0, row - 1), min(self.rows, row + 2)):
            for j in range(max(0, col - 1), min(self.cols, col + 2)):
                if (i, j) != cell:
                    neighbours.append(self.curr_generation[i][j])
        return neighbours

    def get_next_generation(self) -> Grid:
        # Copy from previous assignment
        new_grid = copy.deepcopy(self.grid)
        for i in range(self.rows):
            for j in range(self.cols):
                if (self.curr_generation[i][j] == 0) and sum(self.get_neighbours((i, j))) == 3:
                    new_grid[i][j] = 1
                elif (self.curr_generation[i][j] == 1) and (
                    sum(self.get_neighbours(i, j)) < 2 or sum(self.get_neighbours(i, j)) > 3
                    ):
                    new_grid[i][j] = 0

        return new_grid

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.prev_generation = copy.deepcopy(self.curr_generation)
        self.curr_generation = self.get_next_generation()
        self.generations += 1
        

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        if self.generations == self.max_generations:
            return True
        else:
            return False

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        if self.prev_generation != self.curr_generation:
            return True
        else:
            return False

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        file = open(filename, "r")
        file_grid = [[int(col) for col in row.strip()] for row in file]
        file.close()

        game = GameOfLife((len(file_grid), len(file_grid[0])))
        game.curr_generation = file_grid
        return game

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        file = open(filename, "w")
        for row in self.curr_generation:
            for col in row:
                file.write(str(col))
            file.write("\n")
        file.close()