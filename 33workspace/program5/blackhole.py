# A Black_Hole is a Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
from ball import Ball
import model


class Black_Hole(Simulton):
    radius = 10
    color = 'black'
    
    def get_radius(self):
        return self.get_dimension()[0]/2
        
    def __init__(self,x,y):
        Simulton.__init__(self,x,y, 2*Black_Hole.radius, 2*Black_Hole.radius)
        self._color = Black_Hole.color
    
    def contains(self, o):
        return self.distance(o.get_location()) <= self.get_radius()
    
    def update(self):
        eaten = model.find(lambda x: isinstance(x, Prey) and self.contains(x))
        for e in eaten:
            model.remove(e)
        return eaten
    
    def display(self, canvas):
        r = self.get_radius()
        canvas.create_oval(self._x-r, self._y-r, self._x+r, self._y+r, fill=self._color )
        

