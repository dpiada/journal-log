from tkinter import *
from datetime import datetime
from tinydb import Query
TODAY = str(datetime.now())[:10]

class Model:
    def __init__(self,container):
        self.tinydb = container.tinydb
    
    @property
    def text(self):
        return self.__text
    
    @text.setter
    def text(self, value):
        self.__text = value

    def get_page(self, day):
        print('into model')
        print(day)
        journalLog = Query()
        print(journalLog)
        return self.tinydb.search(journalLog.day == day)
    
    def save(self):
        table_object = self.tinydb.table('journalLog')
        table_object.insert({'day': TODAY, 'text': self.text})

class View:
    def __init__(self, container):
        # create frame            
        workspace = Frame(container, width=540, height=410)
        workspace.grid(row=0, column=1)
        # create text_widget
        self.text_widget = Text(workspace, font=("Arial", 12), bg="white", fg="black", wrap=WORD)
        self.text_widget.grid(row=0, column=1)
        self.text_widget.config(height=390, width=520)
        self.text_widget.bind('<Control-s>', self.save_page)

        # set the controller
        self.controller = None
        self.set_page(day=TODAY)
    
    def set_controller(self, controller):
        self.controller = controller
    
    def save_page(self, event):
        text = self.text_widget.get(1.0, END)
        if self.controller:
            return self.controller.save(text)
    
    def set_page(self, day):
        if self.controller:
            page = self.controller.get_page(day=TODAY)
            return page

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def get_page(self, day=TODAY):
        text = self.model.get_page(day)
        if text:
            return text

    def save(self, text):
        self.model.text = text
        self.model.save()

class Workspace:
    def __init__(self, container):
        model = Model(container)
        view = View(container)
        controller = Controller(model,view)
        view.set_controller(controller)



