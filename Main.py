import tkinter as tk
from Workspace import Diary
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Journal Log')
        self.geometry("724x410")
        self.resizable(False, False)

        Diary(self)
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
