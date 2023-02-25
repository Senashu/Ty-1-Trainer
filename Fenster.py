import tkinter as tk


class DraggableWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # Remove window decorations
        master.overrideredirect(True)

        # Create a custom close button
        self.close_button = tk.Button(self, bg="black", fg="white", text="x", command=master.destroy)
        self.close_button.pack(side=tk.RIGHT, anchor=tk.NE)

        # Create a label widget to display text
        #self.image = tk.PhotoImage("Downloads/hackerman.jpg")
        self.label = tk.Label(self, text="TY1 Trainer", bg="black", fg="white", padx=0, pady=0)
        self.label.pack(ipady=3.48, side=tk.TOP, fill=tk.BOTH)

        # Bind events to the label
        self.label.bind("<ButtonPress-1>", self.start_drag)
        self.label.bind("<ButtonRelease-1>", self.stop_drag)
        self.label.bind("<B1-Motion>", self.drag)

        # Pack the frame widget
        self.pack(fill=tk.BOTH, expand=True)

    def start_drag(self, event):
        # Capture the mouse position when dragging starts
        self.x = event.x
        self.y = event.y


    def stop_drag(self, event):
        # Stop dragging when the left mouse button is released
        self.x = None
        self.y = None

    def drag(self, event):
        if self.x is not None and self.y is not None:
            # Calculate the new window position based on the mouse position
            x = self.master.winfo_x() + event.x - self.x
            y = self.master.winfo_y() + event.y - self.y
            self.master.geometry("+{}+{}".format(x, y))