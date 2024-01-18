from tkinter import *
from datetime import datetime
TODAY = str(datetime.now())[:10]

class View:
    def __init__(self, container):

        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=4)

        mainFrame = Frame(container)
        mainFrame.grid()

        listFrame = Frame(mainFrame)
        listFrame.grid(sticky=NW)

        dayLabel = Label(listFrame, text="10/08/1993")
        dayLabel.grid(row=0, column=0)
        dayLabel = Label(listFrame, text="11/08/1993")
        dayLabel.grid(row=1, column=0)

        entryFrame = Frame(mainFrame)
        entryFrame.grid(row=0, column=1)
        
        entryValueText = Text(entryFrame, font=("Arial", 12), bg="white", fg="black", wrap=WORD, width=55, height=16)
        entryValueText.grid(padx=5, pady=5)


class Diary:
    def __init__(self, container):
        view = View(container)
