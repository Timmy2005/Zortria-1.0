


import Tkinter
import time
from Tkinter import *

class Zortria(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.launcherInitialize()

    def launcherInitialize(self):
        self.grid()

        startButton = Tkinter.Button(self,text=u"Start Game",
                                command=self.OnButtonClick)
        startButton.grid(column=2,row=0)

        self.labelVariable = Tkinter.StringVar()
        self.label2Variable = Tkinter.StringVar()
        
        label = Tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=1,columnspan=2,sticky='EW')
        
        label2 = Tkinter.Label(self,textvariable=self.label2Variable,
                              anchor="w",fg="white",bg="blue")
        label2.grid(column=0,row=2,columnspan=2,sticky='EW')

        label3 = Tkinter.Label

        self.grid_columnconfigure(0,weight=1)

    def OnButtonClick(self):
        self.labelVariable.set("Running game...")

if __name__ == "__main__":
    app = Zortria(None)
    app.title("Zortria Launcher")
    app.mainloop()
