import tkinter as tk
import math as m
#import threading
from main_gui.windowSetup import window_setup 
from main_gui.programLoop import program_loop 
from main_gui.config_file import configuration
from main_gui.windowUpdate import window_update 
from main_gui.medium_objects.manageGrid import manage_grid
from main_gui.medium_objects.attachSpeed import attach_speed 
from main_gui.basic_objects.Arrow import arrow
from main_gui.basic_objects.textManager import text_manager



windowSetup = window_setup()
loop1 = program_loop(windowSetup.window, windowSetup)

while True:
    windowSetup.window.update()





        