

class window_update:
    'used to update everything- the general_update method calls all of the other updating methods'
    def __init__(self, master, speedObject, leftArrow, rightArrow, hazardLight, updatableTextObjectsList, DdriveModeObject, NdriveModeObject, RdriveModeObject):
        self.master = master
        self.speedObject = speedObject
        self.leftArrow = leftArrow
        self.rightArrow = rightArrow
        self.hazardLight = hazardLight
        self.updatableTextObjectsList = updatableTextObjectsList
        self.DdriveModeObject = DdriveModeObject
        self.NdriveModeObject = NdriveModeObject
        self.RdriveModeObject = RdriveModeObject

    def general_update(self, speedValue, leftIndicationOn, rightIndicationOn, hazardOn, updatingTextValues, driveMode):
        self.speedValue = speedValue
        self.rightIndicationOn = rightIndicationOn
        self.leftIndicationOn = leftIndicationOn
        self.hazardOn = hazardOn
        self.updatingTextValues = updatingTextValues
        self.driveMode = driveMode
        self.arrow_update()
        self.speed_update()
        self.warning_lights_update()
        self.text_update()
        self.drive_mode_update()

    def arrow_update(self):  
        self.leftArrow.update_arrow(self.leftIndicationOn)
        self.rightArrow.update_arrow(self.rightIndicationOn)

    def speed_update(self):
        self.speedObject.attach_values(self.speedValue)

    def warning_lights_update(self):
        if self.hazardOn:
            self.hazardLight.attach_image()

    def text_update(self):
        for i in range(len(self.updatableTextObjectsList)):
            self.updatableTextObjectsList[i].display_text(self.updatingTextValues[i])

    def drive_mode_update(self):
        #self.driveModeObject.display_text(self.driveMode, True, 'grey')
        Dcolour = 'grey11'
        Ncolour = 'grey11'
        Rcolour = 'grey11'
        if self.driveMode == 'D':
            Dcolour = 'white'
        elif self.driveMode == 'N':
            Ncolour = 'white'
        elif self.driveMode == 'R':
            Rcolour = 'white'
    
        self.DdriveModeObject.display_text('D', True, Dcolour)
        self.RdriveModeObject.display_text('R', True, Rcolour)
        self.NdriveModeObject.display_text('N', True, Ncolour)
      



