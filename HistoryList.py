from tkinter import *

class Model:
    def __init__(self, container):
        self.tinydb = container.tinydb

    def get_all(self):
        return self.tinydb.all()

class View:
    def __init__(self, container, model):
        historyList = Frame(container, width=180, height=410)
        historyList.grid(row=0, column=0)
        self.model = model
        print(self.model)
        self.items = self.model.get_all()
        print(self.items)
        for item in self.items:
            Label(container, text=item.day, fg="orange", bg="black", font="ariel").grid(row=list.index(item), column=0)

class HistoryList:
    def __init__(self, container):
        model = Model(container)
        View(container, model)