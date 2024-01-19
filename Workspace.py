from tkinter import *
from datetime import datetime
from tinydb import TinyDB, Query
global selected_day
TODAY = str(datetime.now())[:10]
selected_day = TODAY
class Model:
    def __init__(self):
        self.tinydb = TinyDB('db.json')
        self.set_today()

    def set_today(self):
        PageDay = Query()
        today_page = self.tinydb.search(PageDay.day == TODAY)
        if len(today_page) > 0:
            return today_page[0]
        else:
            text = 'Today is '+ TODAY
            self.tinydb.insert({'day': TODAY, 'text': text})

    def get_days(self):
        all_records = self.tinydb.all()
        days = []
        for record in all_records:
            days.append(record['day'])
        return days

    def get_page_by_day(self, day):
        PageDay = Query()
        return self.tinydb.search(PageDay.day == day)[0]

    def update_page(self, day, text):
        PageDay = Query()
        self.tinydb.update({'text': text}, PageDay.day == day)

    def insert_text(self, text):
        self.tinydb.insert({'day': TODAY, 'text': text})

class View:
    def __init__(self, container, controller):
        self.controller = controller
        self.active_button = IntVar(value=-1) 
        self.buttons = []
        self.selected_day = selected_day

        if self.controller : 
            self.days = self.controller.get_days()
            self.today_page = self.controller.get_page_by_day(day = self.selected_day)['text']

        else:
            self.days = []
            self.today_page = ''
        
        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=4)

        mainFrame = Frame(container)
        mainFrame.grid()

        listFrame = Frame(mainFrame)
        listFrame.grid(sticky=NW, padx=5, pady=5)

        for index, day in enumerate(self.days):
            button = Button(listFrame, text=day, height=1, width=10, borderwidth=0, command=lambda i=index: self.set_day(i))
            button.grid(row=index, column=0, pady=2)
            self.buttons.append(button)

        entryFrame = Frame(mainFrame)

        entryFrame.grid(row=0, column=1)
        
        self.entryValueText = Text(entryFrame, font=("Arial", 12), bg="white", fg="black", wrap=WORD, width=55, height=16)
        self.entryValueText.grid(padx=5, pady=5)
        self.setText(today_page = self.today_page)
        self.entryValueText.bind('<Control-s>', lambda event: self.controller.save(day=selected_day, text = self.entryValueText.get(1.0, END)))

    def set_controller(self, controller):
        self.controller = controller

    def setText(self, today_page):
        self.clear()
        self.entryValueText.insert(END, today_page)

    def clear(self):
        self.entryValueText.delete("1.0", END)
    
    def set_day(self, index):
        self.selected_day = self.days[index]
        self.active_button.set(index)
        self.today_page = self.controller.get_page_by_day(day = self.selected_day)['text']
        self.setText(today_page = self.today_page)

        if self.active_button.get() == index:
            (self.buttons[index]).config(state=ACTIVE)

        else:
            (self.buttons[index]).config(state=NORMAL)

class Controller:
    def __init__(self, model):
        self.model = model

    def get_days(self):
        days = self.model.get_days()
        return days

    def get_page_by_day(self, day):
        page_day = self.model.get_page_by_day(day)
        return page_day

    def get_today_page(self):
        days = self.model.set_today()
        return days

    def save(self, day, text):
        self.model.update_page(day, text)
    

class Diary:
    def __init__(self, container):
        model = Model()
        controller = Controller(model)
        view = View(container, controller)

        view.set_controller(controller)
