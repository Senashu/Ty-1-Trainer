import os
import tkinter as tk
import tkinter.ttk as ttk

from Fenster import DraggableWindow


def normal_glide():
    os.system("python Glide/Normal_Glide.py")
def up_glide_slow():
    os.system("python Glide/up_glide_slow.py")
def up_glide_fast():
    os.system("python Glide/up_glide_fast.py")


class ModMenuGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mod Menu")
        self.root.geometry('200x300')
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
        self.notebook.add(self.frame1, text="Teleport WIP")
        self.notebook.add(self.frame2, text="Fly v1")
        self.notebook.add(self.frame3, text="Speed WIP")

        # Add buttons to frames
        self.button1 = ttk.Button(self.frame1, text="XYZ")
        self.button1.pack(padx=100)

        self.button2 = ttk.Button(self.frame2, text="Normal Glide", command=normal_glide)
        self.button2.pack(padx=10)

        self.button3 = ttk.Button(self.frame2, text="Slow Up-Glide", command=up_glide_slow)
        self.button3.pack(padx=10)

        self.button7 = ttk.Button(self.frame2, text="Fast Up-Glide", command=up_glide_fast)
        self.button7.pack(padx=10)

        self.button4 = ttk.Button(self.frame3, text="Add Mod")
        self.button4.pack(padx=10)

        # Bind a function to the close button
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        # Run GUI
        self.root.mainloop()

    def on_close(self):
        # Hide the window instead of closing it
        self.root.withdraw()
