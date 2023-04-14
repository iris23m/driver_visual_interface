import tkinter as tk

class manage_grid():
    def __init__(self, master, numberRows, numberColumns, spans):
        self.master = master
        self.numberRows = numberRows
        self.numberColumns = numberColumns
        self.spans = spans
        self.canvaslist = [[] for i in range(numberRows)]
        self.completeSpans = [[] for i in range(numberRows)]
        self.create_grid()

    def create_grid(self):
        delete_grid = []
        for x in range(self.numberRows):
            self.master.rowconfigure(x,weight=1, minsize=10)
            for y in range(self.numberColumns):
                self.master.columnconfigure(y, weight=1,minsize=20)
                if [x,y] not in delete_grid:

                    columnSpan, rowSpan = self.manage_cell_merging(delete_grid, x, y)
                    self.create_canvas(x, y, columnSpan, rowSpan)

    def create_canvas(self, x, y, columnSpan, rowSpan):
        canvas= tk.Canvas (
                        master = self.master,
                        bg = "black",
                        highlightthickness=1
                    )
        self.canvaslist[x].append(canvas)

        self.completeSpans[x].append([rowSpan, columnSpan])
        canvas.grid(row = x, column = y,sticky="nsew", columnspan =columnSpan, rowspan=rowSpan)

    def manage_cell_merging(self, delete_grid, x, y):
        try:
            columnSpan = self.spans[str([x,y])][1]
            rowSpan = self.spans[str([x,y])][0]
            for i in range(rowSpan):
                for j in range(columnSpan):
                    a = x+i
                    b = y+j
                    delete_grid.append([a,b])
        except:
            rowSpan = 1
            columnSpan = 1
        return columnSpan,rowSpan
