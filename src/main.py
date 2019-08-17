# coding: utf-8

'''
Sample Tkinter App
'''

import tkinter as tk
import json
from gui.MainWindow import MainWindow


if __name__ == '__main__':

    '''
    main function
    '''

    root = tk.Tk()
    func_dict = dict()
    settings = json.load(open("config/settings.json"))

    app = MainWindow(root, func_dict, settings)
    app.mainloop()
