import tkinter as tk
from typing import List

class Calculator:
    def __init__(self, root, label, display, buttons):
        self.root: tk.Tk = root
        self.label: tk.Label = label
        self.display: tk.Entry = display
        self.buttons: List[List[tk.Button]] = buttons

