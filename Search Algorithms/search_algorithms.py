from graph_builder import *
from util import *

"""
	searchAlgorithm is a general function for depth-first and breadth first search.
	The graph must be a valid random graph as defined in graph_builder.py
	The search type must be a string, either "BFS" or "DFS" defaulting with BFS.
"""
def searchAlgorithm(graph, search_type="BFS"):
	try:
		start = graph.startState()
		#corner case
		if graph.isEnd(start):
			return None, None

		# The backtrace variable is used to keep track of how we arrived at a given node
		#	We are going for speed rather than storage efficiency so some allocated
		#	space may not be used.
		backtrace = []
		for i in range(0, graph.size()):
			backtrace.append([0] * graph.size())
		backtrace[start[0]][start[1]] = -1
		tested_actions = []

		# All that matters here is the queue: this is the only difference between DFS and BFS
		if search_type == "BFS":
			queue = FIFO()
		elif search_type == "DFS":
			queue = LIFO()
		else:
			#some imple error checking
			raise ValueError('Error: search_type input in searchAlgorithm must be '
				+ '"BFS" (Breadth-first search) or "DFS" (Depth-first search)')

		# Add starting nodes to the queue
		queue.add(graph.nextActions(start))
		found = False #if the end has not been found and this has not been changed,
						#there is no path from the start to the end node.

		# The main loop
		while not queue.isEmpty():
			# Get action off of the queue
			action = queue.pop()
			end_state = graph.tryAction(action)
			tested_actions.append(action) #for visualization later

			# If this is the goal, we can stop
			if graph.isEnd(end_state):
				found = True
				backtrace[end_state[0]][end_state[1]] = action[0]
				break
			# Otherwise, make sure we have not already added this node to the queue and
			#	continue
			if backtrace[end_state[0]][end_state[1]] == 0:
				queue.add(graph.nextActions(end_state))
				backtrace[end_state[0]][end_state[1]] = action[0]

		# If found, return the path in a (machine) readable format
		if found:
			item = end_state
			path = [end_state]
			while backtrace[item[0]][item[1]] != -1:
				path = [backtrace[item[0]][item[1]]] + path
				item = backtrace[item[0]][item[1]]
			return path, tested_actions

		# Otherwise, there is no path
		return None, None
	except:
		raise ValueError("Error in function searchAlgorithm: is graph a valid graph "
			+ "as defined in graph_builder.py?")

if __name__ == '__main__':
	# Initialize and run
	graph = Grapher(10)
	path, tested_actions = searchAlgorithm(graph)

	# Feedback
	if path == None:
		print("No path found")
	elif graph.isEnd(path[-1]):
		print("Path found to the end state")
	else:
		print("Error: incorrect path found")

	# For printing purposes
	graph.addOrder(tested_actions)
	graph.addPath(path)
	graph.run()