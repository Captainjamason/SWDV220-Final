###   SWDV 220 - Wk8 Final Project
###   JPD - 2025
###   main.py

import tkinter as tk
from gui import placeElements

def startGUI():
    root = tk.Tk()
    root.title("Creature Creator")
    root.geometry("600x250")

    placeElements(root)

    root.mainloop()

# Start the program.
startGUI()