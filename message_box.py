#!/usr/bin/env python3

import tkinter as tk
from collections import OrderedDict

# From https://stackoverflow.com/a/77853316
# Posted by Poikilos, modified by community. See post 'Timeline' for change history
# Retrieved 2026-10-05, License - CC BY-SA 4.
class MessageWindow(tk.Toplevel):
    """An independent window that can be positioned.
    Based on https://stackoverflow.com/a/53839951/4541104 but configurable.
    """
    def __init__(self, title, message, answers=None, **options):
        parent = options.get('parent')
        if parent:
            super().__init__(parent)
        else:
            super().__init__()
        # self.answer = None  # a result of None would indicate *closed*
        # (doesn't change default behavior much--you could still do "if"
        # on self.answer like with messagebox.askokcancel's return)
        self.answer = False  # imitate messagebox.askokcancel behavior
        # (return False if dialog closed without pressing a button).
        if not answers:
            answers = OrderedDict(OK=True)
        self.details_expanded = False
        self.title(title)
        geometry = options.get('geometry')
        if geometry:
            self.geometry(geometry)
        self.resizable(False, False)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        tk.Label(self, text=message, justify=tk.LEFT, font='TkFixedFont').grid(row=0, column=0, columnspan=3, pady=(7, 7), padx=(7, 7), sticky="ew")
        column = 0
        for text, value in answers.items():
            column += 1
            tk.Button(
                self,
                text=text,
                command=lambda v=value: self.set_value(v),
                # ^ v=value to force early binding (store this value
                #   so value of last iteration isn't used for all).
            ).grid(row=1, column=column, sticky="e")

    def set_value(self, value):
        self.answer = value
        self.destroy()

def message_box(title, message, answers=OrderedDict(OK=True, Cancel=False), **options):
    """A drop-in replacement for askokcancel but you can set x and y.
    For options not listed below, see messagebox.askokcancel documentation.

    Keyword arguments:
        parent (tk.Widget): The window to block.
        geometry (Optional[string]): The window size and/or position
            (not available in messagebox, so a TopLevel is used).
    """
    answer = None
    messagewindow = MessageWindow(
        title,
        message,
        answers,
        **options,
    )
    # See https://stackoverflow.com/a/31439014/4541104
    messagewindow.master.wait_window(messagewindow)
    # ^ Using master allows us to know what Tk to stop without global(s)
    return messagewindow.answer

def debug_window(message, tk_root):
    message_box(" ", message, answers=OrderedDict(OK=True), parent=tk_root, geometry="+{}+{}".format(tk_root.winfo_pointerx(), tk_root.winfo_pointery()))
