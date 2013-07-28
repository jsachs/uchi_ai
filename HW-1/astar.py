"""
Module to implement A* on an adjacency matrix.
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

def astar(graph, heur, start, end):
	C = []  # the closed set
	O = []  # the open set, a priority queue
	finder = {}  # a finder to check what is in the open set
	fscore = [0]*len(graph)
	gscore = [0]*len(graph)

	fscore[start] = gscore[start] + heur[start][end]
	heappush(O, (fscore[start], start, [start]))
	finder[start] = fscore[start]

	while finder:
		c, node, path = heappop(O)
		if c != finder[node]:
			continue
		del finder[node]
		C.append(node)
		if node == end:
			path.reverse()
			return C, path
		for adj in range(len(graph)):
			cost = graph[node][adj]
			if cost:
				gscore_temp = gscore[node] + cost
				fscore_temp = gscore_temp + heur[adj][end]
				if adj in C:
					if gscore_temp >= gscore[adj]:
						continue
				if adj not in finder or gscore_temp < gscore[adj]:
					gscore[adj] = gscore_temp
					fscore[adj] = fscore_temp
					new = [adj]
					for n in path:
						new.append(n)
					heappush(O, (fscore[adj], adj, new))
					finder[adj] = fscore[adj]
	return C, None

	
def main():
	if len(argv) < 3:
		print "Error: program requires cost matrix as command line argument"
		return
	f1 = argv[1]
	f2 = argv[2]
	matrix = read_matrix(f1)
	heur   = read_matrix(f2)
	searched, path = astar(matrix, heur, 0, len(matrix)-1)
	file1 = open('searched.txt','w')
	file2 = open('path.txt','w')

	for node in searched:
		file1.write(str(node) + '\n')
	for node in path:
		file2.write(str(node) + '\n')
	return

if __name__ == '__main__':
	main()

