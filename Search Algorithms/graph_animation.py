import Tkinter as tk

class Grapher(object):
	def __init__(self, graph):
		self.graph = graph
		self.root = tk.Tk()
		self.height = 200
		self.width = 200
		self.node_radius = 15
		self.canvas = tk.Canvas(self.root, width=self.width, height=self.height,
			borderwidth=0, highlightthickness=0, bg="white")
		self.canvas.grid()
	
	def __plotNode(self, x, y, color="grey"):
		self.canvas.create_oval(x - self.node_radius, y - self.node_radius,
			x + self.node_radius, y + self.node_radius, fill=color)

	def __draw(self):
		self.__plotNode(100, 120, "blue")

	def run(self):
		self.__draw()
		self.root.mainloop()

graph = Grapher([])
graph.run()
# canvas.grid()

# def _create_circle(self, x, y, r, **kwargs):
#     return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
# tk.Canvas.create_circle = _create_circle

# canvas.create_circle(100, 120, 50, fill="blue", outline="#DDD", width=4)
# canvas.create_circle(150, 40, 20, fill="#BBB", outline="")
# canvas.create_line(15, 25, 200, 25, width=5, fill="red")

# root.wm_title("Circles and Arcs")
# root.mainloop()