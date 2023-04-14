

class window_update:
    'used to update everything- the general_update method calls all of the other updating methods'
    def __init__(self, master, speedObject, leftArrow, rightArrow, hazardLight):
        self.master = master
        self.speedObject = speedObject
        self.leftArrow = leftArrow
        self.rightArrow = rightArrow
        self.hazardLight = hazardLight

    def general_update(self, speedValue, leftIndicationOn, rightIndicationOn, hazardOn):
        self.speedValue = speedValue
        self.rightIndicationOn = rightIndicationOn
        self.leftIndicationOn = leftIndicationOn
        self.hazardOn = hazardOn
        self.arrow_update()
        self.speed_update()
        self.warning_lights_update()

    def arrow_update(self):  
        self.leftArrow.update_arrow(self.leftIndicationOn)
        self.rightArrow.update_arrow(self.rightIndicationOn)

    def speed_update(self):
        self.speedObject.attach_values(self.speedValue)

    def warning_lights_update(self):
        if self.hazardOn:
            self.hazardLight.attach_image()

