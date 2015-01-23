import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special   import Special


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
running     = False
cycle_count = 0;
simultons   = set();
clicked_button = ''


#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running, cycle_count, balls
    running = False
    cycle_count = 0
    balls = set()


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#tep just one update in the simulation
def step ():
    global running
    if not running:
        running = False
        running = True
    update_all()
    display_all()
    running = False


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global clicked_button
    clicked_button = kind
    

#add the kind of remembered object to the simulation (or remove any objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y): 
    if clicked_button == 'Remove':
        for s in simultons:
            if s.contains((x,y)):
                remove(s)
    else:
        if clicked_button != '':
            add(eval(clicked_button+'({x},{y})'.format(x=x, y=y)))
        
#add simulton s to the simulation
def add(s):
    simultons.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    simultons.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    satisfy = set()
    for s in simultons:
        if p(s):
            satisfy.add(s)
            
    return satisfy


#call update for every simulton in the simulation
def update_all():
    global cycle_count
    if running:
        cycle_count+= 1
        for s in list(simultons):
            s.update()
                
    
#delete from the canvas every simulton in the simulation, and then call display for every
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for s in simultons:
        s.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(cycle_count)+" cycles/"+str(len(simultons))+" simultons")