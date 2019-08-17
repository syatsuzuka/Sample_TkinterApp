# coding: utf-8

'''
Main Window for Sample Tkinter App
'''

import tkinter as tk
import os

class MainWindow(tk.Frame):

    '''
    Main Window class
    '''

    def __init__(self, master, func_dict, settings):

        '''
        init function

        Args:
            master (tk.Tk): TK master
            func_dict (dict): dictionary
            settings (json): setting info 
        '''

        #======= Set Main Window =======

        super().__init__(master)
        self.root = master
        self.func_dict = func_dict
        self.settings = settings
        iconpath = "{0}\{1}".format(os.getcwd(), self.settings["IconFile"])
        self.root.iconbitmap(default=iconpath)
        self.root.title(self.settings["WinTitle"])
        self.root.geometry(self.settings["WinSize"])
        self.createWidgets()

    def createWidgets(self):


        '''
        create gui components
        '''

        #======= Set Main Frame =======

        pos = dict()
        pad = dict()
        pad["x"] = self.settings["PadX"]
        pad["y"] = self.settings["PadY"]


        scrollbar = tk.Scrollbar(self.root)
        scrollbar.pack(side=tk.RIGHT, fill="y")

        winHeader = "{0} {1}".format(self.settings["WinHeader"], self.settings["Version"])
        labelTitle = tk.Label(self.root, text = winHeader, font=self.settings["WinHeaderStyle"])
        labelTitle.pack(fill="x",padx=10, pady=10)
        frame = tk.LabelFrame(self.root, text="Common Component")
        frame.pack(fill="x", padx=10, pady=10)

        #======= 1st Line =======
        #----- Left (Button) -----

        pos["row"] = 0
        pos["col"] = 0

        labelButton = tk.Label(frame, text = "Button")
        labelButton.grid(row=pos["row"], column=pos["col"], padx=pad["x"], pady=pad["y"])
        self.Button = tk.Button(frame, text="Button", command=self.clickButton)
        self.Button.grid(row=pos["row"], column=pos["col"]+1, padx=pad["x"], pady=pad["y"])
        self.labelButtonValue = tk.Label(frame, text = "0")
        self.labelButtonValue.grid(row=pos["row"], column=pos["col"]+2, padx=pad["x"], pady=pad["y"])


        #----- Right (Entry) -----

        pos["row"] = pos["row"]
        pos["col"] = pos["col"]+5

        labelEntry = tk.Label(frame, text = "Entry")
        labelEntry.grid(row=pos["row"], column=pos["col"], padx=pad["x"], pady=pad["y"])
        self.Entry = tk.Entry(frame)
        self.Entry.grid(row=pos["row"], column=pos["col"]+1, padx=pad["x"], pady=pad["y"])
        self.labelEntryValue = tk.Label(frame, text = "")
        self.labelEntryValue.grid(row=pos["row"], column=pos["col"]+2, padx=pad["x"], pady=pad["y"])

        #======= 2nd Line =======

        #----- Left (Checkbutton) -----

        pos["row"] = pos["row"]+1
        pos["col"] = 0

        labelCheckbutton = tk.Label(frame, text = "CheckButton")
        labelCheckbutton.grid(row=pos["row"], column=pos["col"], padx=pad["x"], pady=pad["y"])
        self.Checkbutton = tk.Entry(frame)
        self.Checkbutton.grid(row=pos["row"], column=pos["col"]+1, padx=pad["x"], pady=pad["y"])
        self.labelCheckbuttonValue = tk.Label(frame, text = "")
        self.labelCheckbuttonValue.grid(row=pos["row"], column=pos["col"]+2, padx=pad["x"], pady=pad["y"])

        #----- Right (Text) -----

        pos["row"] = pos["row"]
        pos["col"] = pos["col"] + 5

        labelText = tk.Label(frame, text = "Text")
        labelText.grid(row=pos["row"], column=pos["col"], padx=pad["x"], pady=pad["y"])
        self.Text = tk.Text(frame, height=10, width=30)
        self.Text.grid(row=pos["row"], column=pos["col"]+1, padx=pad["x"], pady=pad["y"])
        self.labelTextValue = tk.Label(frame, text = "")
        self.labelTextValue.grid(row=pos["row"], column=pos["col"]+2, padx=pad["x"], pady=pad["y"])


    def clickButton(self):

        '''
        Click Button event
        '''

        newValue = int(self.labelButtonValue.cget("text"))
        self.labelButtonValue["text"]=str(newValue+1)

    def typeEntry(self):

        '''
        Type Entry event
        '''

        self.labelEntryValue["text"] = self.Entry