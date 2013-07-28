#!/usr/bin/python
"""
Module to implement tic tac toe with alpha-beta pruning.
"""
from sys import argv


class Board(object):
	"""This class represents the board state."""
	def __init__(self, size, wins):
		"""
		- size: the size of the board, read from the text file
		- wins: a list of win paths, read from the text file
		"""
		self.spaces = [0]*size  # the board
		self.paths  = []        # winning paths
		for path in wins:
			self.paths.append(path)
		self.last_move = []     # a list of moves, used for backing up

	def output(self):
		"""Displays current markers on the board."""
		for space, mark in enumerate(self.spaces):
			print str(space+1) + ": ", mark

	def get_free_spaces(self):
		"""Returns a list of free spaces on the board."""
		free = []
		for i, space in enumerate(self.spaces):
			if space == 0:
				free.append(i+1)
		return free

	def check_win(self):
		"""Checks if the Computer or the User has won, or for a draw."""
		for path in self.paths:
			temp = [self.spaces[i-1] for i in path]
			if temp[0] and temp == [temp[0]] * len(temp):
				return temp[0]
		if 0 not in self.spaces:
			# draw
			return 'C'
		return False

	def mark_position(self, space, mark):
		"""Marks an X or O on the board."""
		self.spaces[space-1] = mark
		self.last_move.append(space)

	def undo_last_mark(self):
		"""Removes the previous mark on the board."""
		last = self.last_move.pop()
		self.spaces[last-1] = 0

	def play_game(self, p1, p2):
		"""Main game execution function."""
		for turn in range(len(self.spaces)):
			print "Turn:", turn+1
			if turn%2 == 0:
				# computer move
				p1.move(self)
			else:
				# user move
				p2.move(self)
			check = self.check_win()
			if check:
				if check == 'X': print "Computer wins."
				elif check == 'O': print "User wins."
				else: print "It's a draw."
				self.output()
				for path in self.paths:
					temp = [self.spaces[i-1] for i in path]
					if temp[0] and temp == [temp[0]] * len(temp):
						print path
						return
				return


class Computer(object):
	"""This class represents the computer player."""
	def __init__(self):
		self.mark = 'X'
		self.opp  = 'O'

	def move(self, board):
		board.output()
		best = None
		moves = None

		children = board.get_free_spaces()
		for child in children:
			board.mark_position(child, self.mark)
			score = self.alpha_beta(board)
			board.undo_last_mark()
			if best is None or score > best:
				best = score
				moves = child
		board.mark_position(moves, self.mark)

	def alpha_beta(self, board, alpha = float("-inf"), beta = float("inf")):
		"""Returns the value for the optimal next move."""
		check = board.check_win()
		if check:
			# Objective function
			if check == self.mark: return 1
			elif check == self.opp: return -1
			else: return 0
		last_play = board.spaces[board.last_move[-1]-1]
		children = board.get_free_spaces()
		if last_play == self.opp:
			# Computer to move
			for child in children:
				board.mark_position(child, self.mark)
				alpha = max(alpha, self.alpha_beta(board, alpha, beta))
				board.undo_last_mark()
				if beta <= alpha:
					break
			return alpha
		else:
			# User to move
			for child in children:
				board.mark_position(child, self.opp)
				beta = min(beta, self.alpha_beta(board, alpha, beta))
				board.undo_last_mark()
				if beta <= alpha:
					break
			return beta


class Human(object):
	"""This class represents the human player."""
	def __init__(self):
		self.mark = 'O'

	def move(self, board):
		while True:
			board.output()
			print "Available moves:", board.get_free_spaces()
			while True:
				try:
					mv = int(raw_input("Select move: "))
					break
				except ValueError:
					print "Not an int, enter a valid move."
			if mv not in board.get_free_spaces():
				print "Invalid move."
			else:
				board.mark_position(mv, self.mark)
				break


def read_board_file(f):
	lines = open(f,'r').readlines()
	size = int(lines[0])
	wins = []
	for line in lines[1:]:
		new = []
		line = list(line[:-1].replace(' ',''))
		for num in line:
			new.append(int(num))
		wins.append(new)
	return size, wins


def main():
	if len(argv) < 2:
		print "Error: program requires command line board file."
		return
	size, wins = read_board_file(argv[1])
	game = Board(size, wins)
	p1 = Computer()
	p2 = Human()
	game.play_game(p1, p2)

if __name__ == '__main__':
	main()

