import tkinter as tk
import math as m
#import threading
from overall.windowSetup import window_setup 
from overall.programLoop import program_loop 
from overall.config_file import configuration
from overall.windowUpdate import window_update 
from overall.medium_objects.manageGrid import manage_grid
from overall.medium_objects.attachSpeed import attach_speed 
from overall.basic_objects.Arrow import arrow
from overall.basic_objects.textManager import text_manager



windowSetup = window_setup()
loop1 = program_loop(windowSetup.window, windowSetup)

while True:
    windowSetup.window.update()





        