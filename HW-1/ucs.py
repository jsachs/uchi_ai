"""
Module to implement UCS on an adjacency matrix.
"""
from heapq import heappush, heappop
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

def ucs(graph, start, end):
	node = start  # root node
	frontier = [] # priority queue
	finder = {}   # entry finder for the pqueue
	explored = [] # explored nodes
	cost = 0

	heappush(frontier, (cost, node, [node]))
	finder[node] = cost

	while frontier:
		# print frontier
		# get lowest cost node on the frontier
		c, node, path = heappop(frontier)
		# check to make sure we have the right cost
		if c != finder[node]:
			continue
		explored.append(node)
		if node == end:
			path.reverse()
			return explored, path
		for adj in range(len(graph)):  # loop over possible adjacent nodes
			cost = graph[node][adj]
			if cost and adj not in explored:  # if there is a path:
				if adj not in finder or finder[adj] > c + cost:
					new = [adj]
					for n in path:
						new.append(n)
					heappush(frontier, (c + cost, adj, new))
					finder[adj] = c + cost
	return explored, None


def main():
	if len(argv) < 2:
		print "Error: program requires cost matrix as command line argument"
		return
	f = argv[1]
	matrix = read_matrix(f)
	searched, path = ucs(matrix, 0, len(matrix)-1)
	file1 = open('searched.txt','w')
	file2 = open('path.txt','w')

	for node in searched:
		file1.write(str(node) + '\n')
	for node in path:
		file2.write(str(node) + '\n')
	return

if __name__ == '__main__':
	main()

