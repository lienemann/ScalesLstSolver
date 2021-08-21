import copy

class ScalesLstSolver:
	SYMBOLS = ['.', '□', 'O', 'Δ', '+', '*']
	NONE = 0
	SQUARE = 1
	CIRCLE = 2
	TRIANGLE = 3
	CROSS = 4
	STAR = 5

	def __init__(self, table_size: int):
		if table_size < 2:
			raise ValueError("Invalid table size")
		self._n = table_size
		self._in_row = [[False] * self._n for _ in range(self._n)]
		self._in_col = [[False] * self._n for _ in range(self._n)]

		self.count_solutions = False
		self.table = [[0] * self._n for _ in range(self._n)]
		self.solution = [[0] * self._n for _ in range(self._n)]
		self.number_of_solutions = 0


	def add_fixed_symbol(self, symbol: int, row: int, col: int):
		if symbol < 0 or symbol > self._n or row < 0 or row >= self._n or col < 0 or col >= self._n:
			raise ValueError("Invalid parameter value")
		if self.table[row][col] == symbol: # noop
			return
		if symbol > 0 and (self._in_row[row][symbol - 1] or self._in_col[col][symbol - 1]):
			raise ValueError("Symbol already present in row or column")
		if self.table[row][col] != 0: # delete old value
			self._in_row[row][self.table[row][col] - 1] = False
			self._in_col[col][self.table[row][col] - 1] = False
		self.table[row][col] = symbol
		if symbol > 0:
			self._in_row[row][symbol - 1] = True
			self._in_col[col][symbol - 1] = True

	def add_fixed_symbol_from_string_list(self, l : list):
		if len(l) != self._n:
			raise ValueError("Wrong number of rows")
		for r in l:
			if len(r) != self._n:
				raise ValueError("Wrong number of columns")
		for i in range(self._n):
			for j in range(self._n):
				try:
					idx = self.SYMBOLS.index(l[i][j])
				except ValueError:
					idx = ScalesLstSolver.NONE
				self.add_fixed_symbol(idx, i, j)


	def print_table(self, solved = True):
		print("\n".join(
			" ".join(
				ScalesLstSolver.SYMBOLS[(self.solution if solved else self.table)[row][col]]
			for col in range(self._n))
		for row in range(self._n)))

	# Place a symbol; return true if solution was found
	def _place(self, symbol: int, column: int) -> bool:
		# self.print_table(False)
		# print(f"symbol: {self.SYMBOLS[symbol]} ({symbol}), column: {column}\n\n" if symbol < self._n else f"column: {column}\n\n")
		if column >= self._n: # Could also be n-1, then we have to reconstruct the last column
			# Solution found!
			if self.count_solutions:
				self.number_of_solutions += 1
				return False # Don't stop search
			else:
				return True # Stop search
		if symbol > self._n:
			return self._place(1, column + 1)
		if self._in_col[column][symbol - 1]:
			return self._place(symbol + 1, column)
		else:
			for row in range(self._n):
				if self.table[row][column] > 0:
					continue
				if self._in_row[row][symbol - 1]:
					continue
				self.table[row][column] = symbol
				self._in_row[row][symbol - 1] = True
				self._in_col[column][symbol - 1] = True

				if self._place(symbol + 1, column):
					return True

				self.table[row][column] = 0
				self._in_row[row][symbol - 1] = False
				self._in_col[column][symbol - 1] = False
		return False

	def solve(self, target_row, target_col):
		if target_row < 0 or target_row >= self._n or target_col < 0 or target_col >= self._n:
			raise ValueError("Invalid parameter value")
		previous_table = copy.deepcopy(self.table)
		previous_in_row = copy.deepcopy(self._in_row)
		self.number_of_solutions = 0

		# Run
		ret = None
		if self._place(1, 0):
			ret = ScalesLstSolver.SYMBOLS[self.table[target_row][target_col]]

		self.solution = self.table
		self.table = previous_table
		self._in_row = previous_in_row

		return ret
