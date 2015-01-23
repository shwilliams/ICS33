# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole
import model

class Pulsator(Black_Hole):
    
    counter = 30
    def __init__(self,x,y):
        self._counter = 0
        Black_Hole.__init__(self,x,y)
    
    def update(self):
        ate = Black_Hole.update(self)    
        if ate:
            self.change_dimension(len(ate), len(ate))
            self._counter = 0
            
        else:
            self._counter +=1
            if self._counter == 30:
                self._counter = 0
                self.change_dimension(-1,-1)
                if self.get_dimension() == (0,0):
                    model.remove(self)
        return ate