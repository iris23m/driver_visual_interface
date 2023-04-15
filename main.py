from main_gui.windowSetup import window_setup 
from main_gui.programLoop import program_loop 
from main_gui.getData import dataFetcher

windowSetup = window_setup()
dataFetcher = dataFetcher()
loop1 = program_loop(windowSetup.window, windowSetup, dataFetcher)

while True:
    windowSetup.window.update()





        