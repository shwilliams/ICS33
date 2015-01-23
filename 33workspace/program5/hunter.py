# A Hunter is both Mobile_Simulton and Pulsator; it updates
#   like a Pulsator, but also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from prey import Prey
from math import atan2
from blackhole import Black_Hole
import model


class Hunter(Pulsator,Mobile_Simulton):
    
    def __init__(self,x,y):
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self, x, y, self._width, self._height, 0, 5)
        self.randomize_angle()
    
    def visible_distance(self,xy):
        return self.distance(xy) <= 200
    
    def angle_to(self,x,y):
        return atan2(y-self._y, x-self._x)
    
    def update(self):
        eat = Pulsator.update(self)
        Mobile_Simulton.update(self)
        aim = model.find(lambda x: isinstance(x, Prey) and self.visible_distance(x.get_location()))
        
        if aim:
            first_target =  min([s.get_location() for s in aim], key = lambda x: self.distance(x))
            x,y = first_target
            self.set_angle(self.angle_to(x,y))
            
        return eat  
            