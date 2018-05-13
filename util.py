###############################################################
# util.py =================================================== #
# This is the implementation of multiple data structures ==== #
# Most of them are standard, this is how to make them ======= #
# 	from scratch. =========================================== #
###############################################################

#Errors
QUEUE_VALUE_ERROR = 'Error: Queue is only implemented for lists, integers, and floats'

"""
	isValid is a helper function that checks if the input is valid
	Returns an array of the items in arg is all of them are valid
	Throws error if any of the items are invalid
"""
def isValid(arg):
	arr = [] #the array that will be returned
	if type(arg) is list:
		# run through items in the list if it is a list
		for item in arg:
			#check if valid
			if type(item) is int or type(item) is float:
				arr.append(item) #if so, append
			else:
				raise ValueError(QUEUE_VALUE_ERROR) #if not, throw this error
	# check if it is a single item
	elif type(arg) is int or type(arg) is float:
		arr.append(arg) #if so, append
	else:
		raise ValueError(QUEUE_VALUE_ERROR) #if not, throw this error
	return arr

"""
	Queue is a parent class for general Queues
"""
class Queue(object):
	#constructor
	def __init__(self, arg=None):
		super(Queue, self).__init__()
		if arg is None:
			self.Q = []
		else:
			self.Q = isValid(arg)

	#add new element(s) to the queue
	def add(self, arg):
		self.Q = self.Q + isValid(arg)

	#return the number of elements in the queue
	def length(self):
		return len(self.Q)

	#returns a boolean that is true if the queue is empty
	def isEmpty(self):
		return len(self.Q) == 0

"""
	First in, first out (FIFO) queue inherits from Queue
"""
class FIFO(Queue):
	#constructor that calls Queue
	def __init__(self, arg=None):

	#remove first element from the list (FIFO) and return it
	#	returns None is it is empty
	def pop(self):
		if len(self.Q) < 1:
			return None
		item = self.Q[0]
		self.Q = self.Q[1:]
		return item

"""
	Last in, first out (LIFO) queue inherits from Queue
"""
class LIFO(Queue):
	#constructor that calls Queue
	def __init__(self, arg=None):
		Queue.__init__(self, arg)

	#remove last element from the list (FIFO) and return it
	#	returns None is it is empty
	def pop(self):
		if len(self.Q) < 1:
			return None
		item = self.Q[-1]
		self.Q = self.Q[:-1]
		return item

"""
	Priority queue inherits from Queue
"""
class Priority(Queue):
	#constructor that calls Queue
	def __init__(self):
		Queue.__init__(self, None)
		self.items = []

	#adds an element to the list with a given priority
	def add(self, item, priority):
		added = False
		for itr in range(0, len(self.Q)):
			if self.Q[itr][0] > priority:
				self.Q = self.Q[:itr] + [(priority, item)] + self.Q[itr:]
				return None
		self.Q.append((priority, item))

	#remove last element from the list (FIFO) and return it
	#	returns None is it is empty
	def pop(self):
		if len(self.Q) < 1:
			return None
		item = self.Q[0]
		self.Q = self.Q[0:]
		return item