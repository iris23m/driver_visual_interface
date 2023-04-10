import math as m
import tkinter as tk

class arrow:
    def __init__(self, master, a_direction, a_location, a_grid_width, a_grid_height, scale):
        self.master = master
        self.direction = a_direction
        self.location = a_location
        self.gridwidth = a_grid_width
        self.gridheight = a_grid_height
        self.scale = scale
        self.previouslyOn = False
        self.get_coords()

    def get_coords(self):
        'works out the coords in the grid space to put the arrow'
        self.arrow_y = self.gridheight/2
        self.arrowhead1 = self.gridwidth *0.15*self.scale
        self.arrowhead3 = self.gridheight *0.07*self.scale
        self.arrowhead2 = m.sqrt((self.arrowhead1**2)+(self.arrowhead3**2))
        self.arrow_width = self.gridheight *0.2*self.scale
        if self.direction == 'left':
            self.arrow_x1 = self.gridwidth * 0.1
            self.arrow_x2 = self.gridwidth * (0.1+(0.4*self.scale))
            self.arrowside = tk.FIRST
        elif self.direction == 'right':
            self.arrow_x1 =  self.gridwidth*(0.9-(0.4*self.scale))
            self.arrow_x2 = self.gridwidth*0.9
            self.arrowside = tk.LAST
        self.draw_arrow('grey11')

    def draw_arrow(self, colour):
        'Function to draw the arrow shape, need to give the colour but it takes the coords from the object'
        self.location.create_line(self.arrow_x1, self.arrow_y, self.arrow_x2, self.arrow_y, 
                                  width = self.arrow_width, fill = colour, arrow=self.arrowside, 
                                  arrowshape=[self.arrowhead1,self.arrowhead2,self.arrowhead3])
   
    def flash_arrow_on(self): 
        'starts the indicator flashing, automatically stops when the status variable gets set to False'
        self.colour = 'green'  
        self.draw_arrow(self.colour)
        self.master.after(500, self.flash_arrow_off)
    
    def flash_arrow_off(self):
        'Part of the flashing function- the two functions feedback to each other'
        self.colour = 'grey11'
        self.draw_arrow(self.colour)
        if self.isOn:
            self.master.after(500, self.flash_arrow_on)
            self.previouslyOn = True
        else:
            self.previouslyOn = False

    def update_arrow(self, isOn):
        self.isOn = isOn
        if self.isOn and self.previouslyOn == False:
            self.flash_arrow_on()