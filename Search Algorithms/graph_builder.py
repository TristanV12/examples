###############################################################
# graph_builder.py ========================================== #
# This is an example of how to build graphs in python. ====== #
# For more information on python or the packages used visit:  #
###############################################################

# Imports
import random # for creating random graph

"""
	Graph2D is a class that creates a random graph of size graph_size x graph_size
	It is meant to be an easy to view graph, so it allows motion in only two
		directions: up/down, left/right.
"""
class Graph2D:
	# Constructor
	def __init__(self, graph_size, weighted=False):
		self.graph = []
		self.outstring = ""
		self.start = (int(random.random() * graph_size), int(random.random() * graph_size))
		self.end = (int(random.random() * graph_size), int(random.random() * graph_size))
		# Build 0'd out graph
		for x in range(0, graph_size):
			self.graph.append([0] * graph_size)
		for x in range(0, graph_size):
			for y in range(0, graph_size):
				# 8 = up, 4 = down, 2 = left, 1 = right
				# I'm using binary because it is the easiest way for me to
				#	think about it, but there are other ways to do it.
				# 3 = 1 + 2 = left, right vs 12 = 8 + 4 = up, down

				# undirected: checks if the nodes above and to the left are
				#	connected, then adds a connection back if so
				if x != 0:
					self.graph[y][x] += (2 * (self.graph[y][x - 1] % 2))
				if y != 0:
					self.graph[y][x] += (8 * ((self.graph[y - 1][x] // 4) % 2))

				# Randomly assigns other connections with probability 3/4
				if x != graph_size - 1:
					self.graph[y][x] += (1 * (random.random() < .75))
				if y != graph_size - 1:
					self.graph[y][x] += (4 * (random.random() < .75))

		# Builds the outsring for further sanity later
		for y in range(0, (graph_size * 2) - 1):
			for x in range(0, graph_size):
				if y % 2 == 0:
					if (x, y // 2) == self.start:
						self.outstring += 's'
					elif (x, y // 2) == self.end:
						self.outstring += 'e'
					else:
						self.outstring += 'o'
					if self.graph[y // 2][x] % 2 == 1:
						self.outstring += '-'
					else:
						self.outstring += ' '
				else:
					if (self.graph[y // 2][x] // 4) % 2 == 1:
						self.outstring += '|'
					else:
						self.outstring += ' '
					self.outstring += ' '
			if y != (graph_size - 1) * 2:
				self.outstring += '\n'

	# Getter that checks if we are at the start state. Probably redundant
	def isStart(self, state):
		return state == self.start

	# Getter that checks if we are at the goal state
	def isEnd(self, state):
		return state == self.end

	# Helper function that checks if a given state is on the board
	#	Returns true if the state is INvalid
	def __invalidState(self, state):
		try:
			size = len(self.graph)
			return state[0] >= size or state[1] >= size or state[0] < 0 or state[1] < 0
		except:
			return True

	# Getter that returns the start state
	def startState(self):
		return self.start

	# Getter that returns following actions of a state
	def nextActions(self, state):
		actions = []
		if self.__invalidState(state):
			return []
		#make sure the request is valid
		try:
			#return actions in order
			num = self.graph[state[1], state[0]]
			if num > 7:
				actions.append((state, "UP"))
			if (num // 4) % 2 == 1:
				actions.append((state, "DOWN"))
			if (num // 2) % 2 == 1:
				actions.append((state, "LEFT"))
			if num % 2 == 1:
				actions.append((state, "RIGHT"))
		except:
			#malformed, return empty array
			return []

	# Getter that returns the state as a result of an action
	def tryAction(self, action):
		#make sure request is well-formed
		try:
			#helper variables
			state = action[0]
			act = action[1]
			#make sure we're in the graph
			if self.__invalidState(state):
				return None
			num = self.graph[state[1], state[0]]
			#return new state
			if act == "UP" and num > 7:
				return (state[0], state[1] - 1)
			if act == "DOWN" and (num // 4) % 2 == 1:
				return (state[0], state[1] + 1)
			if act == "LEFT" and (num // 2) % 2 == 1:
				return (state[0] - 1, state[1])
			if act == "RIGHT" and num % 2 == 1:
				return (state[0] + 1, state[1])
			return None
		except:
			#malformed request: return None
			return None

	# Just for sanity, this returns a string version of the graph
	def __str__(self):
		return self.outstring

if __name__ == '__main__':
	graph = Graph2D(10, False)
	print(graph)