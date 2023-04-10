
class text_manager:
    def __init__(self, master, gridCoord, grid, window_width, window_height):
        self.master = master
        self.gridCoord = gridCoord
        self.grid = grid
        self.length = 0
        self.window_width = window_width
        self.window_height = window_height

    def coords_size(self, text):
        for t in text:
            self.length += 1
        boxWidth = (self.window_width/self.grid.numberColumns)*self.grid.completeSpans[self.gridCoord[0]][self.gridCoord[1]][1]
        boxHeight = (self.window_height/self.grid.numberRows)*self.grid.completeSpans[self.gridCoord[0]][self.gridCoord[1]][0]
        y = boxHeight/2
        x = boxWidth/2
        #size = int((boxwidth/self.length)* 1)
        size = int(13*(boxHeight/50))
        font = 'Arial ' + str(size) #+ ' bold'
        canvasObject = self.grid.canvaslist[self.gridCoord[0]][self.gridCoord[1]]
        canvasObject.create_text(x, y, text=text, fill="white", font=font)
