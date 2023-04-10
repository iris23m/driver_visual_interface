from overall.config_file import configuration
from overall.windowUpdate import window_update 
from overall.medium_objects.manageGrid import manage_grid
from overall.medium_objects.attachSpeed import attach_speed 
from overall.basic_objects.numberDisplay import number_display 
from overall.basic_objects.Arrow import arrow
from overall.basic_objects.textManager import text_manager




import tkinter as tk


class window_setup:
    def __init__(self):
        config_values = configuration()
        self.windowWidth = config_values.WINDOW_WIDTH
        self.windowHeight = config_values.WINDOW_HEIGHT
        self.window = tk.Tk()
        geo = str(config_values.WINDOW_WIDTH) + 'x' + str(config_values.WINDOW_HEIGHT)
        self.window.geometry(geo)
        self.grid = manage_grid(self.window, config_values.ROWS, config_values.COLUMNS , config_values.SPANS )
        self.gridWidth = self.windowWidth/config_values.COLUMNS
        self.gridHeight = self.windowHeight/config_values.ROWS
        status = True
        self.create_left_arrow()
        self.create_right_arrow()
        self.create_speed()
        self.create_base_text()
        self.update_window()

    def create_left_arrow(self):
        leftArrowDirection = 'left'
        leftArrowCanvas = self.grid.canvaslist[0][0]
        self.leftArrow = arrow(self.window, leftArrowDirection, leftArrowCanvas, self.gridWidth, self.gridHeight,1.5)
     
    def create_right_arrow(self):
        rightArrowDirection = 'right'
        rightArrowCanvas = self.grid.canvaslist[0][7]
        self.rightArrow = arrow(self.window, rightArrowDirection, rightArrowCanvas, self.gridWidth, self.gridHeight,1.5)

    def create_speed(self):
        self.speedObject = attach_speed(self.window, [1,0], self.grid, self.windowWidth, self.windowHeight)

    def create_base_text(self):
            battDrainText = text_manager(self.window, [4, 0], self.grid, self.windowWidth, self.windowHeight)
            battDrainText.coords_size('Batt. drain: ')

            solarPowerText = text_manager(self.window, [5, 0], self.grid, self.windowWidth, self.windowHeight)
            solarPowerText.coords_size('Solar power: ')

            battDrainUnitsText = text_manager(self.window, [5, 2], self.grid, self.windowWidth, self.windowHeight)
            battDrainUnitsText.coords_size('kW')

            solarPowerUnitsText = text_manager(self.window, [4, 2], self.grid, self.windowWidth, self.windowHeight)
            solarPowerUnitsText.coords_size('kW')

    def update_window(self):
        self.windowUpdater = window_update(self.window, self.speedObject, self.leftArrow, self.rightArrow)
