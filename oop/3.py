

class SurfaceAreaVolume:

def __init__(self, l, w, h):

self.length = l

self.width = w

self.height = h

def surface_area(self):

return 2*(self.length*self.width + self.length*self.height+ self.width*self.height)

def volume(self):

return self.length*self.width*self.height

obj = SurfaceAreaVolume(2, 3, 4)

print("Surface Area:", obj.surface_area())

print("Volume:", obj.volume())