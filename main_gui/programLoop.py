class program_loop:
    def __init__(self, master, windowSetup):
        self.master = master
        self.windowSetup = windowSetup
        self.update1()
 
    def update1(self): 
        'updates the values and schedules the other update function to be called- the two functions pass between each other'
        self.inputSpeed =160
        self.inputLeftIndicatorOn = True
        self.inputRightIndicatorOn = False
        self.windowSetup.windowUpdater.general_update(int(self.inputSpeed), bool(self.inputLeftIndicatorOn), bool(self.inputRightIndicatorOn))
        
        self.master.after(500, self.update2)

    
    def update2(self):
        'updates the values and schedules the first function again'
        self.inputSpeed = 161
        self.inputLeftIndicatorOn = True
        self.inputRightIndicatorOn = False
        self.windowSetup.windowUpdater.general_update(int(self.inputSpeed), bool(self.inputLeftIndicatorOn), bool(self.inputRightIndicatorOn))

        self.master.after(500, self.update1)
    


    