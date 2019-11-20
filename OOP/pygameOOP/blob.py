import random

class Blob:

    def __init__(self, color, x_boundary, y_boundary, size_range=(4,8), mov_range=(-1, 2)):
        self.size = random.randrange(size_range[0], size_range[1])
        self.color = color
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.mov_range = mov_range
        self.x = random.randrange(0, self.x_boundary)
        self.y = random.randrange(0, self.y_boundary)

    def __repr__(self):
        return 'Blob({}, {}, ({},{}))'.format(  self.color,
                                                self.size,
                                                self.x,
                                                self.y)

    def __str__(self):
        return 'Blob of color:{}, size: {}, location: ({},{})'.format(  self.color,
                                                                        self.size,
                                                                        self.x,
                                                                        self.y)

    def move(self):
        self.move_x = random.randrange(self.mov_range[0], self.mov_range[1])
        self.move_y = random.randrange(self.mov_range[0], self.mov_range[1])
        self.x += self.move_x
        self.y += self.move_y

    def checkbounds(self):
        if self.x < 0: self.x = 0
        elif self.x > self.x_boundary: self.x = self.x_boundary
        if self.y < 0: self.y = 0
        elif self.y > self.y_boundary: self.y = self.y_boundary
