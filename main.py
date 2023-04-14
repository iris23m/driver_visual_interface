from main_gui.windowSetup import window_setup 
from main_gui.programLoop import program_loop 

windowSetup = window_setup()
loop1 = program_loop(windowSetup.window, windowSetup)

while True:
    windowSetup.window.update()





        