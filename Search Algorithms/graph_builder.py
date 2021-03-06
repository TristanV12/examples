###############################################################
# graph_builder.py ========================================== #
# This is an example of how to build graphs in python. ====== #
# For more information on python or the packages used visit:  #
###############################################################

# Imports
import random # for creating random graph
import Tkinter as tk # for animation purposes
import time

"""
	Graph2D is a class that creates a random graph of size graph_size x graph_size
	It is meant to be an easy to view graph, so it allows motion in only two
		directions: up/down, left/right.
"""
class Graph2D:
	# Constructor, max_weight is 0 if the graph is unweighted
	def __init__(self, graph_size, max_weight=1):
		# error checking
		if type(max_weight) != int or max_weight < 1:
			raise ValueError("Error: max_weight in Graph2D must be an integer greater "
				+ "than or equal to 1 (equal to 1 for unweighted graphs)")
		if type(graph_size) != int or graph_size < 2:
			raise ValueError("Error: graph_size in Graph2d must be an integer greater "
				+ "than or equal to 2")
		self.graph = []
		self.outstring = ""
		self.start = (int(random.random() * (graph_size - 1)),
			int(random.random() * (graph_size - 1)))
		self.end = (int(random.random() * (graph_size - 1)),
			int(random.random() * (graph_size - 1)))
		self.order = None
		self.weighted = max_weight > 1
		# Build 0'd out graph
		for x in range(0, graph_size):
			self.graph.append([])
			for y in range(0, graph_size):
				self.graph[-1].append([0, 0])

		for x in range(0, graph_size):
			for y in range(0, graph_size):
				# 8 = up, 4 = down, 2 = left, 1 = right
				# I'm using binary because it is the easiest way for me to
				#	think about it, but there are other ways to do it.
				# 3 = 1 + 2 = left, right vs 12 = 8 + 4 = up, down

				# # undirected: checks if the nodes above and to the left are
				# #	connected, then adds a connection back if so
				# if x != 0:
				# 	self.graph[y][x] += self.graph[y][x - 1]
				# if y != 0:
				# 	self.graph[y][x] += (8 * ((self.graph[y - 1][x] // 4) % 2))

				# Randomly assigns down, right connections with probability 3/4
				if x != graph_size - 1:
					if max_weight > 1:
						weight = int((max_weight - 1) * random.random()) + 1
					else:
						weight = 1
					self.graph[y][x][0] = (weight * (random.random() < .75))
				if y != graph_size - 1:
					if max_weight > 1:
						weight = int(max_weight * random.random())
					else:
						weight = 1
					self.graph[y][x][1] = (weight * (random.random() < .75))

		# Builds the outstring for further sanity later
		#	Boards greater than 100x100 take too long and are
		#	pointless to represent in this way
		if graph_size <= 100 and max_weight < 10:
			y_range = ((graph_size - 1) * ((2 * (not self.weighted))+(4 * self.weighted))) + 1
			if self.weighted:
				div = 4
			else:
				div = 2
			for y in range(0, y_range):
				for x in range(0, graph_size):
					if y % div == 0:
						if (x, y // div) == self.start:
							self.outstring += 's'
						elif (x, y // div) == self.end:
							self.outstring += 'e'
						else:
							self.outstring += 'o'
						if self.weighted:
							if self.graph[y // div][x][0] != 0:
								self.outstring += '-' + str(self.graph[y // div][x][0]) + '-'
							else:
								self.outstring += '   '
						else:
							if self.graph[y // div][x][0] != 0:
								self.outstring += '-'
							else:
								self.outstring += ' '
					else:
						if self.weighted and y % 2 != 0:
							if self.graph[y // 4][x][1] != 0:
								self.outstring += '|'
							else:
								self.outstring += ' '
							self.outstring += '   '
						elif self.weighted:
							if self.graph[y // 4][x][1] != 0:
								self.outstring += str(self.graph[y // 4][x][1])
							else:
								self.outstring += ' '
							self.outstring += '   '
						else:
							if self.graph[y // 2][x][1] != 0:
								self.outstring += '|'
							else:
								self.outstring += ' '
							self.outstring += ' '
				if y != y_range - 1:
					self.outstring += '\n'
		elif max_weight < 10:
			self.outstring = "Graph too large to represent"
		else:
			self.outstring = "max_weight is too large to represent the graph"

	# Getter that checks if we are at the start state. Probably redundant
	def isStart(self, state):
		return state == self.start

	# Getter that checks if we are at the goal state
	def isEnd(self, state):
		return state == self.end

	# Getter that returns the number of columns/rows in the graph
	def size(self):
		return len(self.graph)

	# Helper function that checks if a given state is on the board
	#	Returns true if the state is INvalid
	def _invalidState(self, state):
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
		if self._invalidState(state):
			return []
		#make sure the request is valid
		try:
			#return actions in order
			num = self.graph[state[1]][state[0]]
			if state[1] > 0 and self.graph[state[1] - 1][state[0]][1] != 0:
				actions.append([state, "UP", self.graph[state[1] - 1][state[0]][1]])
			if self.graph[state[1]][state[0]][1] != 0:
				actions.append([state, "DOWN", self.graph[state[1]][state[0]][1]])
			if state[0] > 0 and self.graph[state[1]][state[0] - 1][0] != 0:
				actions.append([state, "LEFT", self.graph[state[1]][state[0] - 1][0]])
			if self.graph[state[1]][state[0]][0] != 0:
				actions.append([state, "RIGHT", self.graph[state[1]][state[0]][0]])
			return actions
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
			if self._invalidState(state):
				return None
			#return new state
			if act == "UP" and self.graph[state[1] - 1][state[0]][1] != 0:
				return (state[0], state[1] - 1)
			if act == "DOWN" and self.graph[state[1]][state[0]][1] != 0:
				return (state[0], state[1] + 1)
			if act == "LEFT" and self.graph[state[1]][state[0] - 1][0] != 0:
				return (state[0] - 1, state[1])
			if act == "RIGHT" and self.graph[state[1]][state[0]][0] != 0:
				return (state[0] + 1, state[1])
			return None
		except:
			#malformed request: return None
			return None

	# Just for sanity, this returns a string version of the graph
	def __str__(self):
		return self.outstring

"""
	Grapher is a class that builds a visualization of the graph and the algorithms
"""
class Grapher(Graph2D):
	# Constructor
	def __init__(self, graph_size, max_weight=1, animate_speed=1, show_dists=False):
		Graph2D.__init__(self, graph_size, max_weight)
		self.root = tk.Tk()
		self.height = min(50*graph_size, 700)
		self.width = min(50*graph_size, 700)
		self.node_radius = self.height / (5 * graph_size)
		self.canvas = tk.Canvas(self.root, width=self.width, height=self.height,
			borderwidth=0, highlightthickness=0, bg="white")
		self.canvas.grid()
		self.order = None
		self.path = None
		self.offset = self.node_radius * 5
		self.animate_speed = animate_speed
		self.show_dists = show_dists

	# Helper function to find start/end of lines
	def __locsLines(self, start, end):
		x_loc = (start[0] * self.offset) + (2.25 * self.node_radius)
		y_loc = (start[1] * self.offset) + (2.25 * self.node_radius)
		x_loc2 = (end[0] * self.offset) + (2.25 * self.node_radius)
		y_loc2 = (end[1] * self.offset) + (2.25 * self.node_radius)

		if y_loc == y_loc2:
			if x_loc > x_loc2:
				x_loc = x_loc - self.node_radius
				x_loc2 = x_loc2 + self.node_radius
			else:
				x_loc = x_loc + self.node_radius
				x_loc2 = x_loc2 - self.node_radius

		if x_loc == x_loc2:
			if y_loc > y_loc2:
				y_loc = y_loc - self.node_radius
				y_loc2 = y_loc2 + self.node_radius
			else:
				y_loc = y_loc + self.node_radius
				y_loc2 = y_loc2 - self.node_radius
		return x_loc, y_loc, x_loc2, y_loc2

	# Helper function that plots a circle of radius self.radius at the center (x, y)
	def __plotNode(self, x, y, color="grey", over_text="", text_color="black"):
		self.canvas.create_oval(x - self.node_radius, y - self.node_radius,
			x + self.node_radius, y + self.node_radius, fill=color)
		self.canvas.create_text(x, y, text=over_text, fill="black")

	# Helper function for drawing a line with two nodes at the end
	#	This is helpful for animating the path
	def __drawSingle(self, start, end, line_color, edge_weight=0, node_weights=0):
		# locations of start and end nodes
		x_loc = (start[0] * self.offset) + (2.25 * self.node_radius)
		y_loc = (start[1] * self.offset) + (2.25 * self.node_radius)
		x_loc2 = (end[0] * self.offset) + (2.25 * self.node_radius)
		y_loc2 = (end[1] * self.offset) + (2.25 * self.node_radius)
		text_x = min(x_loc, x_loc2) + abs((x_loc - x_loc2) * .5)
		text_y = min(y_loc, y_loc2) + abs((y_loc - y_loc2) * .5)

		# Draw the line
		self.canvas.create_line(x_loc, y_loc, x_loc2,
			y_loc2, width=2, fill=line_color)

		# Label weight of the edge, decide whether or not to label nodes
		over_text = ("", "")
		if self.weighted:
			self.canvas.create_text(text_x, text_y, text=str(edge_weight), fill=line_color)
			over_text = (str(node_weights[0]), str(node_weights[1]))

		# Color the first node, should never be end
		color = "grey"
		if self.isStart(start):
			color = "blue"
		self.__plotNode(x_loc, y_loc, color,
						over_text=over_text[0], text_color=line_color) #plot

		# Color the second node
		color = "grey"
		if self.isStart(end):
			color = "blue"
		elif self.isEnd(end):
			color = "red"
		self.__plotNode(x_loc2, y_loc2, color,
						over_text=over_text[1], text_color=line_color) #plot

	# Function that draws everything
	def __draw(self):
		# For simplification later
		infinity = 	u"\u221E"

		# Iterate through each node to draw edges first (so there are not overlap issues)
		for x in range(0, len(self.graph)):
			for y in range(0, len(self.graph)):
				# Get location of first node and the connected nodes
				x_loc = (x * self.offset) + (2.25 * self.node_radius)
				y_loc = (y * self.offset) + (2.25 * self.node_radius)
				actions = self.nextActions((x, y))

				# Draw a line to each connected node
				for action in actions:
					color = "black"
					if action[1] == "DOWN":
						x_loc2 = (x * self.offset) + (2.25 * self.node_radius)
						y_loc2 = ((y + 1) * self.offset) + (2.25 * self.node_radius)
					elif action[1] == "RIGHT":
						x_loc2 = ((x + 1) * self.offset) + (2.25 * self.node_radius)
						y_loc2 = (y * self.offset) + (2.25 * self.node_radius)
					else:
						continue
					self.canvas.create_line(x_loc, y_loc, x_loc2, y_loc2, width=1, fill=color)
					if self.weighted:
						text_x = min(x_loc, x_loc2) + abs((x_loc - x_loc2) * .5)
						text_y = min(y_loc, y_loc2) + abs((y_loc - y_loc2) * .5)
						self.canvas.create_text(text_x, text_y,
							text=str(action[2]), fill="black")

		# Draw the actual nodes
		for x in range(0, len(self.graph)):
			for y in range(0, len(self.graph)):
				x_loc = (x * self.offset) + (2.25 * self.node_radius)
				y_loc = (y * self.offset) + (2.25 * self.node_radius)
				color = "grey"
				if self.isStart((x, y)):
					color = "blue"
				if self.isEnd((x, y)):
					color = "red"
				self.__plotNode(x_loc, y_loc, color)
				if self.weighted:
					self.canvas.create_text(x_loc, y_loc, text=infinity)

		self.canvas.update() #push

		# Animate algorithm
		if self.order != None:
			prev_action = None
			for action in self.order:
				if prev_action != None:
					start = prev_action[0]
					end = self.tryAction(prev_action)
					try:
						if len(prev_action[3]) == 2:
							weights = prev_action[3]
						else:
							weights = 0
					except:
						weights = 0
					self.__drawSingle(start, end, "grey", edge_weight=prev_action[2],
						node_weights=weights)
				prev_action = action
				start = action[0]
				end = self.tryAction(action)
				try:
					if len(prev_action[3]) == 2:
						weights = prev_action[3]
					else:
						weights = (0, 0)
				except:
					weights = (0, 0)
				self.__drawSingle(start, end, "red", edge_weight=prev_action[2],
					node_weights=weights)
				time.sleep(self.animate_speed)
				self.canvas.update()
			if prev_action != None:
				start = prev_action[0]
				end = self.tryAction(prev_action)
				try:
					if len(prev_action[3]) == 2:
						weights = prev_action[3]
					else:
						weights = 0
				except:
					weights = 0
				self.__drawSingle(start, end, "grey", edge_weight=prev_action[2],
					node_weights=weights)

		# Outline path
		if self.path != None:
			path_color = "red"
			node_color = "blue"
			x_loc, y_loc, x_loc2, y_loc2 = self.__locsLines(self.path[0], self.path[1])
			self.canvas.create_line(x_loc, y_loc, x_loc2, y_loc2, width=2, fill=path_color)
			node_color = "grey"
			for i in range(1, len(self.path) - 1):
				first = self.path[i]
				second = self.path[i + 1]
				x_loc, y_loc, x_loc2, y_loc2 = self.__locsLines(first, second)

				self.canvas.create_line(x_loc, y_loc, x_loc2, y_loc2, width=2, fill=path_color)			time.sleep(self.animate_speed)
			self.canvas.update()

	# Add an oder of viewed actions
	#	The error checking could run faster, but it is safe
	# TODO: update error checking
	def addOrder(self, order):
		for action in order:
			if action[:3] not in self.nextActions(action[0]):
				return None
		self.order = order

	# Add a path from start to end node (or between any nodes)
	#	first check that all states are valid: return none if not
	def addPath(self, path):
		for state in path:
			if self._invalidState(state):
				return None
		self.path = path

	# Draw the graph
	def run(self):
		if self.size() > 100:
			print("Graph is too big to draw")
			return
		self.__draw()
		self.root.mainloop()