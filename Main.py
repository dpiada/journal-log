import tkinter as tk
from tkinter import *
from HistoryList import HistoryList
from Workspace import Workspace
from tinydb import TinyDB

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Journal Log')
        self.geometry("720x410")
        self.resizable(0, 0)
        self.tinydb = TinyDB('journalLog.json')

        HistoryList(self)
        Workspace(self)

if __name__ == "__main__":
    app = App()
    app.mainloop()