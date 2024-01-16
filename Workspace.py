from tkinter import *

class Workspace:
    def __init__(self, container):
        right_frame = Frame(container, width=540, height=410)
        right_frame.grid(row=0, column=1)
        text_widget = Text(right_frame, font=("Arial", 12), bg="white", fg="black", wrap=WORD)
        text_widget.pack(fill=BOTH, expand=True)
        text_widget.insert(END, "Welcome to the Text Editor!")
        text_widget.config(height=390, width=520)



