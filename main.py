import tkinter as tk
from tkinter import *
from HistoryList import HistoryList
from Workspace import Workspace

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Journal')
        self.geometry("720x410")
        self.resizable(0, 0)
        HistoryList(self)
        Workspace(self)

if __name__ == "__main__":
    app = App()
    app.mainloop()
