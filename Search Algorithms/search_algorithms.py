from graph_builder import *
from util import *
import argparse

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


"""
	djikstra is a general function for Djikstra's search algorithm.
	The graph must be a valid random graph weighted graph as defined in graph_builder.py
"""
def djikstra(graph):
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
			backtrace.append([-1] * graph.size())
		backtrace[start[0]][start[1]] = 0
		tested_actions = []

		# We use a priority queue for this algorithm
		queue = Priority()

		# Add starting nodes to the queue
		nextActions = graph.nextActions(start)
		for action in nextActions:
			queue.add(item=action, priority=backtrace[start[0]][start[1]] + action[2])
		found = False #if the end has not been found and this has not been changed,
						#there is no path from the start to the end node.

		# The main loop
		while not queue.isEmpty():
			# Get action off of the queue
			action = queue.pop()
			start_state = action[1][0]
			end_state = graph.tryAction(action[1])
			act = action[1]
			new_weight = backtrace[start_state[0]][start_state[1]] + action[1][2]
			if backtrace[end_state[0]][end_state[1]] != -1:
				new_weight = min(new_weight, backtrace[end_state[0]][end_state[1]])
			act.append((backtrace[start_state[0]][start_state[1]], new_weight))
				
			tested_actions.append(act) #for visualization later

			# If this is the goal, we can stop
			if graph.isEnd(end_state):
				found = True
				backtrace[end_state[0]][end_state[1]] = action[0]
				break
			# Otherwise, make sure we have not already added this node to the queue and
			#	continue
			if (backtrace[end_state[0]][end_state[1]] == -1
				or backtrace[end_state[0]][end_state[1]] > action[0]):
				backtrace[end_state[0]][end_state[1]] = action[0]
				nextActions = graph.nextActions(end_state)
				for action in nextActions:
					queue.add(item=action,
						priority=backtrace[end_state[0]][end_state[1]] + action[2])

		# If found, return the path in a (machine) readable format
		if found:
			path = [end_state]
			while not graph.isStart(path[0]):
				item = path[0]
				min_back = backtrace[item[0]][item[1]]
				min_path = item
				nextActions = graph.nextActions(item)
				for action in nextActions:
					new_end = graph.tryAction(action)
					if (min_back > backtrace[new_end[0]][new_end[1]]
						and backtrace[new_end[0]][new_end[1]] != -1):

						min_back = backtrace[new_end[0]][new_end[1]]
						min_path = new_end
				path = [min_path] + path
			return path, tested_actions

		# Otherwise, there is no path
		return None, None
	except:
		raise ValueError("Error in function djikstra: is graph a valid graph "
			+ "as defined in graph_builder.py?")

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Run tests on BFS and DFS algorithms')

	parser.add_argument('--speed', metavar='speed', type=float, nargs=1, default=[1],
	                    help='Number of seconds it each trial is shown (1 is default)')

	parser.add_argument('--graph_size', metavar='graph_size', type=int, nargs=1, default=[10],
	                    help='Size of the graph: ' +
	                    	 'graph_size x graph_size nodes (10 is default)')

	parser.add_argument('--max_weight', metavar='max_weight', type=int, nargs=1, default=[1],
	                    help='Maximum weight an edge can have in the graph. ' +
	                    	 'Cannot be less than 1, must be an integer (1 is default)')

	parser.add_argument('--alg', metavar='alg', type=str, nargs=1, default=["BFS"],
	                    help='Algorithm to use. ' +
	                    	 'Can be "BFS", "DFS", or "Djikstra" (BFS is default)')

	args = parser.parse_args()

	# Initialize the graph
	graph = Grapher(args.graph_size[0], args.max_weight[0], animate_speed=args.speed[0])

	if args.alg[0] == "BFS":
		path, tested_actions = searchAlgorithm(graph)
	elif args.alg[0] == "DFS":
		path, tested_actions = searchAlgorithm(graph, "DFS")
	elif args.alg[0] == "Djikstra":
		path, tested_actions = djikstra(graph)
	else:
		raise ValueError("Error: alg must be one of 'BFS', 'DFS', or 'Djikstra' "
			+ "(without quotes)")

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