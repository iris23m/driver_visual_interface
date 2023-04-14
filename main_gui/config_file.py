class configuration:
    'key parameters to change the layout of the window'
    def __init__(self):
        self.setup()

    def setup(self):
        self.WINDOW_HEIGHT = 300
        self.WINDOW_WIDTH = 400
        self.ROWS = 9
        self.COLUMNS = 8
        #key needs to have a space between , and 2nd number to work
        self.SPANS = {'[1, 0]':[3,6], '[0, 3]':[1,2], '[4, 0]':[1,2], 
         '[5, 0]':[1,2]}

        


        