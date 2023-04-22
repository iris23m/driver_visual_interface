from main_gui.config_file import configuration
from main_gui.windowUpdate import window_update 
from main_gui.medium_objects.manageGrid import manage_grid
from main_gui.medium_objects.attachSpeed import attach_speed 
from main_gui.basic_objects.numberDisplay import number_display 
from main_gui.basic_objects.Arrow import arrow
from main_gui.basic_objects.textManager import text_manager
from main_gui.basic_objects.displayImage import display_image

import tkinter as tk

class window_setup:
    'sets up the window, creates all the objects, creates the window updater from the windows_update class that can be used later'
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
        self.updatableTextObjectsList = []
        status = True
    
        
        self.create_left_arrow()
        self.create_right_arrow()
        self.create_speed()
        self.create_battDrain()
        self.create_solarPower()
        self.create_busVolts()
        self.create_bmuStatus()
        self.create_motorStatuses()
        self.create_ivtStatuses()
        self.create_mpptStatuses()
        self.create_driveMode()
        self.create_warning_lights()
        self.update_window()

    def create_left_arrow(self):
        leftArrowDirection = 'left'
        leftArrowCanvas = self.grid.canvaslist[0][0]
        self.leftArrow = arrow(self.window, leftArrowDirection, leftArrowCanvas, self.gridWidth, self.gridHeight,1.5)
     
    def create_right_arrow(self):
        rightArrowDirection = 'right'
        rightArrowCanvas = self.grid.canvaslist[0][6]
        self.rightArrow = arrow(self.window, rightArrowDirection, rightArrowCanvas, self.gridWidth, self.gridHeight,1.5)

    def create_speed(self):
        self.speedObject = attach_speed(self.window, [1,0], self.grid, self.windowWidth, self.windowHeight)

    def create_battDrain(self):
            battDrainText = text_manager(self.window, [5, 0], self.grid, self.windowWidth, self.windowHeight)
            battDrainText.display_text('Batt. drain: ')
            battDrainUnitsText = text_manager(self.window, [5, 2], self.grid, self.windowWidth, self.windowHeight)
            battDrainUnitsText.display_text('kW')
            self.battDrainValueText = text_manager(self.window, [5, 1], self.grid, self.windowWidth, self.windowHeight)
            self.updatableTextObjectsList.append(self.battDrainValueText)

    def create_solarPower(self):
            solarPowerText = text_manager(self.window, [6, 0], self.grid, self.windowWidth, self.windowHeight)
            solarPowerText.display_text('Solar power: ')
            solarPowerUnitsText = text_manager(self.window, [6, 2], self.grid, self.windowWidth, self.windowHeight)
            solarPowerUnitsText.display_text('kW')
            self.solarPowerValueText = text_manager(self.window, [6, 1], self.grid, self.windowWidth, self.windowHeight)
            self.updatableTextObjectsList.append(self.solarPowerValueText)    

    def create_busVolts(self):
            busVoltsText = text_manager(self.window, [7, 0], self.grid, self.windowWidth, self.windowHeight)
            busVoltsText.display_text('Bus volts: ')
            busVoltsUnitsText = text_manager(self.window, [7, 2], self.grid, self.windowWidth, self.windowHeight)
            busVoltsUnitsText.display_text('kW')
            self.busVoltsValueText = text_manager(self.window, [7, 1], self.grid, self.windowWidth, self.windowHeight)
            self.updatableTextObjectsList.append(self.busVoltsValueText)     

    def create_bmuStatus(self):
            bmuStatusText = text_manager(self.window, [8, 0], self.grid, self.windowWidth, self.windowHeight)
            bmuStatusText.display_text('BMU: ')
    
            self.bmuStatusValueText = text_manager(self.window, [8, 1], self.grid, self.windowWidth, self.windowHeight)
            self.updatableTextObjectsList.append(self.bmuStatusValueText)       

    def create_motorStatuses(self):
            LMotorStatusText = text_manager(self.window, [8, 3], self.grid, self.windowWidth, self.windowHeight)
            LMotorStatusText.display_text('L Motor: ')
    
            self.LMotorStatusValueText = text_manager(self.window, [8, 4], self.grid, self.windowWidth, self.windowHeight)
            self.updatableTextObjectsList.append(self.LMotorStatusValueText)       

            RMotorStatusText = text_manager(self.window, [9, 3], self.grid, self.windowWidth, self.windowHeight)
            RMotorStatusText.display_text('R Motor: ')
    
            self.RMotorStatusValueText = text_manager(self.window, [9, 4], self.grid, self.windowWidth, self.windowHeight)
            self.updatableTextObjectsList.append(self.RMotorStatusValueText) 

    def create_ivtStatuses(self):
            ivtFrontStatusText = text_manager(self.window, [9, 0], self.grid, self.windowWidth, self.windowHeight)
            ivtFrontStatusText.display_text('IVT Front: ')
    
            self.ivtFrontStatusValueText = text_manager(self.window, [9, 1], self.grid, self.windowWidth, self.windowHeight)
            self.updatableTextObjectsList.append(self.ivtFrontStatusValueText)       

            ivtRearStatusText = text_manager(self.window, [10, 0], self.grid, self.windowWidth, self.windowHeight)
            ivtRearStatusText.display_text('IVT Rear: ')
    
            self.ivtRearStatusValueText = text_manager(self.window, [10, 1], self.grid, self.windowWidth, self.windowHeight)
            self.updatableTextObjectsList.append(self.ivtRearStatusValueText) 

    def create_mpptStatuses(self):
            mppt1StatusText = text_manager(self.window, [5, 3], self.grid, self.windowWidth, self.windowHeight)
            mppt1StatusText.display_text('MPPT1: ')
    
            self.mppt1StatusValueText = text_manager(self.window, [5, 4], self.grid, self.windowWidth, self.windowHeight)
            self.updatableTextObjectsList.append(self.mppt1StatusValueText)    

            mppt2StatusText = text_manager(self.window, [6, 3], self.grid, self.windowWidth, self.windowHeight)
            mppt2StatusText.display_text('MPPT2: ')
    
            self.mppt2StatusValueText = text_manager(self.window, [6, 4], self.grid, self.windowWidth, self.windowHeight)
            self.updatableTextObjectsList.append(self.mppt2StatusValueText)   

            mppt3StatusText = text_manager(self.window, [7, 3], self.grid, self.windowWidth, self.windowHeight)
            mppt3StatusText.display_text('MPPT3: ')
    
            self.mppt3StatusValueText = text_manager(self.window, [7, 4], self.grid, self.windowWidth, self.windowHeight)
            self.updatableTextObjectsList.append(self.mppt3StatusValueText) 

    def create_driveMode(self):
            self.driveModeObject = text_manager(self.window, [11, 3], self.grid, self.windowWidth, self.windowHeight)         

    def create_warning_lights(self):
        self.hazardLight = display_image(self.window, "hazard_light.png" , [0,3], self.grid, [25,25], self.windowWidth, self.windowHeight)

    def update_window(self):
        self.windowUpdater = window_update(self.window, self.speedObject, self.leftArrow, self.rightArrow,self.hazardLight, self.updatableTextObjectsList, self.driveModeObject)
