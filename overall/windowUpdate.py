class window_update:
    def __init__(self, master, speedObject, leftArrow, rightArrow):
        self.master = master
        self.speedObject = speedObject
        self.leftArrow = leftArrow
        self.rightArrow = rightArrow

    def general_update(self, speedValue, leftIndicationOn, rightIndicationOn):
        self.speedValue = speedValue
        self.rightIndicationOn = rightIndicationOn
        self.leftIndicationOn = leftIndicationOn
        self.arrow_update()
        self.speed_update()

    def arrow_update(self):  
        self.leftArrow.update_arrow(self.leftIndicationOn)
        self.rightArrow.update_arrow(self.rightIndicationOn)

    def speed_update(self):
        self.speedObject.attach_values(self.speedValue)
