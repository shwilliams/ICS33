#When special eats Prey, it divides. It tracks nearest Prey within their vision.
#Place a single Special in a lot of prey and watch how it devours the entire population
from hunter import Hunter
import math
import model

class Special(Hunter):
    def __init__(self, x, y):
        Hunter.__init__(self, x, y)
        self._color = 'green'
    
    def visible_distance(self, xy):
        return Hunter.visible_distance(self, xy) and abs(self.get_angle()-self.angle_to(xy[0], xy[1])) <= math.pi/4 
    
    def update(self):
        eat = Hunter.update(self)
        if eat:
            daughter_ameba = Special(self._x, self._y)
            daughter_ameba.set_dimension(self._width, self._height)
            daughter_ameba.set_angle(self._angle+math.pi)
            model.add(daughter_ameba)   
            