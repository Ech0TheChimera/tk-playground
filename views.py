import tkinter as tk
from tkinter import ttk

class mainApp(tk.Tk):
    def __inint__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
