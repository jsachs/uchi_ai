"""
Module to implement DFS on an adjacency matrix.
"""
from sys import argv

def read_matrix(fname):
	ret = []
	matrix = open(fname,'r').readlines()
	for line in matrix:
		if line[0] == '#' or line in ['\n','\r\n']:
			# comment line or blank line
			continue
		# store the adjacency matrix as a list of lists
		# nodes are stored as strings
		new = []
		line = list(line[:-1].replace(' ',''))
		for num in line:
			new.append(int(num))
		ret.append(new)
	return ret

def dfs(cost, start, end):
	stack = []
	searched = []
	stack.append([start])
	searched.append(start)

	while stack:
		nodes = stack.pop()
		node = nodes[0]
		if node == end:
			nodes.reverse()
			return searched, nodes
		for adj in range(len(cost)):
			is_path = cost[node][adj]
			if is_path and adj not in searched:
				new = [adj]
				for n in nodes:
					new.append(n)
				stack.append(new)
				searched.append(adj)
	return searched, None


def main():
	if len(argv) < 2:
		print "Error: program requires cost matrix as command line argument"
		return
	f = argv[1]
	matrix = read_matrix(f)
	searched, path = dfs(matrix, 0, len(matrix)-1)
	file1 = open('searched.txt','w')
	file2 = open('path.txt','w')

	for node in searched:
		file1.write(str(node) + '\n')
	for node in path:
		file2.write(str(node) + '\n')
	return

if __name__ == '__main__':
	main()