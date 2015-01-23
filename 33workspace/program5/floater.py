# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


#from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random
from random import uniform


class Floater(Prey):
    radius = 5
    speed = 5
    angle = 0
    color = 'red'    
    def __init__(self,x,y):
        Prey.__init__(self,x,y,2*Floater.radius,2*Floater.radius,Floater.angle,Floater.speed)
        self.randomize_angle()
    
    def _valid_speed(self):
        return 3 <= self._speed <= 7
    
    def _floater_speed(self):
        self._speed += uniform(-0.5,0.5)
    
    def _floater_angle(self):
        self._angle += uniform(-0.5,0.5)

    def update(self):
        probability = random()
        if probability <= 0.3:
            self._floater_speed()
            self._floater_angle()

            while not self._valid_speed():
                self._floater_speed()
        
        Prey.update(self)
    
    def display(self, canvas):
        canvas.create_oval(self._x-Floater.radius, self._y-Floater.radius, self._x+Floater.radius, self._y+Floater.radius, fill=Floater.color )