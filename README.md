# Overview
This is a simple diary application implemented in Python using the Tkinter library for the graphical user interface, TinyDB for lightweight database storage.

## Features
Date-based Pages: Each day has its own page, and you can navigate between days using buttons in the user interface.

**Text Entry**: The application allows you to enter and edit text for a specific day.

**Persistence**: Diary entries are stored in a TinyDB database (db.json), ensuring that your entries persist across sessions.

## Components
1. Model \
The Model class is responsible for handling data storage and retrieval using TinyDB. It includes methods for setting the current day, retrieving all days, fetching a specific day's page, updating a page, and inserting new text.

2. View \
The View class handles the graphical user interface using Tkinter. It consists of a list of buttons for each day, a text entry area, and methods for updating the UI based on user interactions.

3. Controller \
The Controller class acts as an intermediary between the Model and View. It provides methods for retrieving days, fetching a page by day, getting today's page, and saving changes.

4. Diary \
The Diary class initializes the Model, Controller, and View to create the complete diary application.

## Usage
Run the application using the provided Python script.\
Navigate between days using the buttons on the left.\
Enter or edit text in the text entry area.\
Save changes using the keyboard shortcut Ctrl + S.\

## Dependencies
Tkinter: Python's de facto standard GUI library.\
TinyDB: A lightweight, document-oriented database for Python.\
datetime: A module for working with dates and times.\

## Installation
Clone the repository: git clone https://github.com/dpiada/journal-log.git \
Install dependencies: pip install -r requirements.txt \
Run the application: python3 main.py 


