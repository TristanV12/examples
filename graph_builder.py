###############################################################
# =========================================================== #
# graph_builder.py ========================================== #
# This is an example of how to build graphs in python. ====== #
# For more information on python or the packages used visit:  #
###############################################################

# Imports
import random # for creating random graph

class Graph:
	def __init__(self, graph_size, weighted=True):
		self.graph = []
		self.outstring = ""
		for x in range(0, graph_size):
			self.graph.append([])
			for y in range(0, graph_size):
				if y == x:
					self.graph[x].append(0)
				if weighted:
					self.graph[x].append(int(random.random() * 5)) # adds number between 0 and 5
				else:
					self.graph[x].append(int(random.random() * 2)) # adds 0 or 1 randomly
				self.outstring += str(self.graph[x][y])
				if y == graph_size - 1 and x != graph_size - 1:
					self.outstring += "\n"
				else:
					self.outstring += " "

	def __str__(self):
		return self.outstring

if __name__ == '__main__':
	graph = Graph(10, False)
	print(graph)