import pygame as py
from constants import COLS, ROWS, SQUARE_SIZE, BLACK 

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.pos = (row * SQUARE_SIZE, col * SQUARE_SIZE)
        self.neighbor_positions = []

    def render(self, canvas):
        py.draw.rect(canvas, BLACK, (self.col * SQUARE_SIZE,
                                                  self.row * SQUARE_SIZE, SQUARE_SIZE,
                                                  SQUARE_SIZE))

    def init_adjacency_list(self, grid):
        up, down, left, right = None, None, None, None
        #This means we have a cell in the top row, so we can't go up
        if self.row - 1 >= 0:
            up = grid[self.row - 1][self.col]
        #This means we have a cell in the bottom row, so we can't go down
        if self.row + 1 != ROWS:
            down = grid[self.row + 1][self.col]
        #This means we have a cell in the left col, so we can't go left
        if self.col - 1 >= 0:
            left = grid[self.row][self.col - 1]
        if self.col + 1 != COLS:
            right = grid[self.row][self.col + 1]
        return [up, down, left, right]
