import os
import tkinter as tk
import tkinter.ttk as ttk
from Fenster import DraggableWindow


def Glide():
    os.system("python Changed/Glide.py")
def Glide2():
    os.system("python Changed/Glide2.py")
def Speed():
    os.system("python Changed/Speed.py")
def Speed2():
        os.system("python Changed/Speed2.py")
def Health():
        os.system("python Changed/Health.py")
def Health2():
    os.system("python Changed/Health2.py")
def Jump():
    os.system("python Changed/Jump.py")
def Jump2():
    os.system("python Changed/Jump2.py")



class ModMenuGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mod Menu")
        self.root.geometry('200x300')
        self.root.lift()
        self.root.attributes('-topmost', True)
        # Create a draggable window
        window = DraggableWindow(self.root)

        # Create notebook widget
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(ipady=230, side=tk.TOP, fill=tk.BOTH, anchor=tk.S)

        # Create five frames as tabs
        self.frame1 = ttk.Frame(self.notebook)
        self.frame2 = ttk.Frame(self.notebook)
        self.frame3 = ttk.Frame(self.notebook)

        # Add tabs to notebook
        self.notebook.add(self.frame1, text="Main")
        self.notebook.add(self.frame2, text="Teleport WIP")
        # Add label to frames
        self.label1 = ttk.Label(self.frame1, text="Alt+Enter for better experience")
        self.label1.place(x=10, y=230)

        self.label2 = ttk.Label(self.frame1, text="Glide Speed")
        self.label2.place(x=10, y=5)

        self.label3 = ttk.Label(self.frame1, text="Run Speed")
        self.label3.place(x=10, y=60)

        self.label4 = ttk.Label(self.frame1, text="Jump")
        self.label4.place(x=10, y=115)

        self.label5 = ttk.Label(self.frame1, text="Health")
        self.label5.place(x=10, y=170)

        # Add buttons to frames
        self.button1 = ttk.Button(self.frame1, text="Normal", command=Glide)
        self.button1.place(x=10, y=25)

        self.button2 = ttk.Button(self.frame1, text="Up", command=Glide2)
        self.button2.place(x=100, y=25)

        self.button3 = ttk.Button(self.frame1, text="Normal", command=Speed)
        self.button3.place(x=10, y=80)

        self.button4 = ttk.Button(self.frame1, text="Fast", command=Speed2)
        self.button4.place(x=100, y=80)

        self.button5 = ttk.Button(self.frame1, text="Normal", command=Jump)
        self.button5.place(x=10, y=135)

        self.button5 = ttk.Button(self.frame1, text="Super", command=Jump2)
        self.button5.place(x=100, y=135)

        self.button5 = ttk.Button(self.frame1, text="Add", command=Health)
        self.button5.place(x=10, y=190)

        self.button5 = ttk.Button(self.frame1, text="Sub", command=Health2)
        self.button5.place(x=100, y=190)




        # Bind a function to the close button
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        # Run GUI
        self.root.mainloop()

    def on_close(self):
        # Hide the window instead of closing it
        self.root.withdraw()
