class program_loop:
    'main loop to keep updating everything- uses the window_update object that was first created in the window_setup object '
    def __init__(self, master, windowSetup):
        self.master = master
        self.windowSetup = windowSetup
        self.update1()
 
    def update1(self): 
        'updates the values and schedules the other update function to be called- the two functions pass between each other'
        #the idea is that these would eventually be updated by some CAN function
        self.inputSpeed =160
        self.inputLeftIndicatorOn = True
        self.inputRightIndicatorOn = False
        self.hazardsOn = True
        self.battDrain = '100'
        self.solarPower = '20'
        self.updatingTextValues= ['100', '20', '1', 'NO COMMS','NO COMMS','NO COMMS','NO COMMS','NO COMMS',
                                  'NO COMMS','NO COMMS','NO COMMS']
        self.driveMode = 'N'
        self.windowSetup.windowUpdater.general_update(int(self.inputSpeed), bool(self.inputLeftIndicatorOn),
                                                       bool(self.inputRightIndicatorOn), bool(self.hazardsOn),
                                                         self.updatingTextValues, self.driveMode)
        
        self.master.after(500, self.update2)

    
    def update2(self):
        'updates the values and schedules the first function again'
        self.inputSpeed = 161
        self.inputLeftIndicatorOn = True
        self.inputRightIndicatorOn = False
        self.hazardsOn = True
        self.updatingTextValues = ['100', '20', '1', 'NO COMMS','NO COMMS','NO COMMS','NO COMMS','NO COMMS',
                                  'NO COMMS','NO COMMS','NO COMMS', 'NO COMMS']
        self.driveMode = 'N'
        self.windowSetup.windowUpdater.general_update(int(self.inputSpeed), bool(self.inputLeftIndicatorOn),
                                                       bool(self.inputRightIndicatorOn), bool(self.hazardsOn),
                                                         self.updatingTextValues, self.driveMode)

        self.master.after(500, self.update1)
    


    