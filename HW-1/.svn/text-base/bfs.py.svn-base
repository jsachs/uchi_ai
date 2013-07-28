"""
Module to implement BFS on an adjacency matrix.
"""
from sys import argv

#TODO: Make robust (in case of no path)

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

def bfs(cost, start, end):
	queue = []             # a queue of paths
	searched = []          # a list of searched nodes
	marks = [0]*len(cost)  # a list of marks for nodes

	queue.append([start])
	searched.append(start)
	marks[start] = 1

	while queue:
		# get the first path from the queue
		path = queue.pop(0)
		# take the last node from the path
		node = path[0]
		# check if we made it to the end
		if node == end:
			# returns a tuple of lists for providing output
			path.reverse()
			return searched, path
		# construct a new path for adjacent, unvisited nodes
		# add these paths to the queue
		for adj in range(len(cost)):
			is_path = cost[node][adj] 
			if is_path and not marks[adj]:
				marks[adj] = 1
				searched.append(adj)
				new = []
				new.append(adj)
				for n in path:
					new.append(n)
				queue.append(new)
	return searched, None

def main():
	if len(argv) < 2:
		print "Error: program requires cost matrix as command line argument"
		return
	f = argv[1]
	matrix = read_matrix(f)
	searched, path = bfs(matrix, 0, len(matrix)-1)
	file1 = open('searched.txt','w')
	file2 = open('path.txt','w')

	for node in searched:
		file1.write(str(node) + '\n')
	for node in path:
		file2.write(str(node) + '\n')
	return

if __name__ == '__main__':
	main()

