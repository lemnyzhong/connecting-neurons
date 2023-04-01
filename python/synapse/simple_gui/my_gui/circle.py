class Circle:
    def __init__(self, canvas, x, y, radius, colour):
        self.canvas = canvas
        self.radius = radius
        self.colour = colour
        
        self.x = x
        self.y = y

        self.canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill=colour)

    def move(self, x, y):
        self.x += x
        self.y += y

        