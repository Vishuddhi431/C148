#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 19:20:19 2023

@author: vishuddhimakeshwaran
"""

from tkinter import *
import random 

root = Tk()
root.title("Random List Generator")
root.geometry("400x500")
root.configure(background = "lightcyan")

label_list = Label(root, bg = "lightcyan", fg = "midnightblue")
label_list.place(relx = 0.5, rely = 0.4, anchor = CENTER)
label_sorted_list = Label(root, bg = "lightcyan", fg = "midnightblue")
label_sorted_list.place(relx = 0.5, rely = 0.5, anchor = CENTER)

def genList():
    randomList = random.sample(range(0, 50), 5)
    print(randomList)
    label_list["text"] = "List: " + str(randomList)
    randomList.sort()
    print(randomList)
    label_sorted_list["text"] = "Sorted List: " + str(randomList)

button1 = Button(root, text = "Generate Random List", command = genList, bg = "midnightblue", fg = "midnightblue")   
button1.place(relx = 0.5, rely = 0.3, anchor = CENTER)

root.mainloop()

#https://www.loom.com/share/7d35a5d56d1a43dcbe10f66e5780d829?sid=1cc288b2-2623-4040-b750-aa4fb3bd3915
