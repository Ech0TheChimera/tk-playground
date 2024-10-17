import tkinter as tk
from tkinter import ttk

class mainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        #init the tkinter container
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        
        #configure the grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        #initialize the frames
        self.frames = {}
        
        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(StartPage)

    # Raises the frame to the top
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
# StartPage class IS-A tk.Frame
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        #Create a label widget that says Start Page
        label = ttk.Label(self, text="Start Page")
        
        #tell the label where in the grid it belongs
        label.grid(row=2, column=2, padx=10, pady=10)
        
        #Create a button widget that says Visit Page 1
        button = ttk.Button(self, text="Visit Page 1", 
                            command=lambda: controller.show_frame(PageOne))
        
        #tell the button where in the grid it belongs  
        button.grid(row=3, column=2, padx=10, pady=10)
        
        #Create a button widget that says Visit Page 2
        button2 = ttk.Button(self, text="Visit Page 2",
                             command=lambda: controller.show_frame(PageTwo))
        
        #tell the button where in the grid it belongs
        button2.grid(row=4, column=2, padx=10, pady=10)

# PageOne class IS-A tk.Frame
class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        #Create a label widget that says Page One
        label = ttk.Label(self, text="Page One")
        
        #tell the label where in the grid it belongs
        label.grid(row=2, column=2, padx=10, pady=10)
        
        #Create a button widget that says Back to Home
        button = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        
        #tell the button where in the grid it belongs
        button.grid(row=3, column=2, padx=10, pady=10)

# PageTwo class IS-A tk.Frame
class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        #Create a label widget that says Page Two
        label = ttk.Label(self, text="Page Two")
        
        #tell the label where in the grid it belongs
        label.grid(row=2, column=2, padx=10, pady=10)
        
        #Create a button widget that says Back to Home
        button = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        
        #tell the button where in the grid it belongs
        button.grid(row=3, column=2, padx=10, pady=10)