
import numpy as np

def simulate(rows, cols, steps, live_cells):
	board = conway(rows, cols, steps, live_cells)
	board.run()

class conway():
    def __init__(self, rows, cols, steps, live_cells):
    	self.rows = rows
    	self.cols = cols
    	self.steps = steps
    	self.live_cells = live_cells
    	self.grid = np.empty((rows+2, cols+2), dtype='str')
    	self.grid[:] = ' '
    	for el in live_cells:
    		self.grid[el[0]+1][el[1]+1] = '*'

    def printGrid(self):
    	"""Prints the board, exclusing the outermost 
    	"""
    	print("-" * (self.cols + 2))
    	for idx in range(1, self.rows+1):
    		# print(idx)
    		print('|' + ''.join(self.grid[idx][1:-1]) + '|')
    	print("-" * (self.cols + 2) + '\n')

    def simulateStep(self):
    	newGrid = np.empty((self.rows+2, self.cols+2), dtype='str')
    	newGrid[:] = ' '
    	for i in range(1, self.rows+1):
    		for j in range(1, self.cols+1):
    			count = [self.grid[i-1][j-1], self.grid[i-1][j], self.grid[i-1][j+1], 
    				 self.grid[i][j-1], self.grid[i][j+1],
    				 self.grid[i+1][j-1], self.grid[i+1][j], self.grid[i+1][j+1]].count('*')
    			if count == 3:
    				newGrid[i][j] = '*'
    			elif self.grid[i][j] == '*' and count == 2:
    				newGrid[i][j] = '*'
    	self.grid = newGrid

    def run(self):
    	for i in range(self.steps):
    		self.simulateStep()
    		self.printGrid()

