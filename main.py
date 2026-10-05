#!/usr/bin/env python3

import sys
import subprocess
import tkinter as tk
from message_box import debug_window

def main():
    root = tk.Tk()
    root.withdraw()

    arg = sys.argv[1] # "1", "2", "3", or "4"
    #debug_window(arg, root)

    window_list_output = subprocess.run(['wmctrl', '-lx'], stdout=subprocess.PIPE)
    window_list_result = window_list_output.stdout.decode('utf-8')
    #debug_window(window_list_result, root)

    # convert each line as an entry
    # parse each line:
    # Window id, Virtual desktop number that the window belongs to (-1 means all virtual desktops), WM_CLASS, Client machine name, Window title (the window title can have spaces in it)

    # to convert a hex string to int:
    # int("deadbeef", 16)
    # int("0xdeadbeef", 0) # if string is suffixed with 0x

    focus_output = subprocess.run(['xdotool', 'getwindowfocus', '-f'], stdout=subprocess.PIPE)
    focused_window_id_decimal = int(focus_output.stdout.decode('utf-8'))
    #debug_window(hex(focused_window_id_decimal), root)

    # this will focus on the window whose WM_CLASS is "jetbrains-rider.jetbrains-rider"
    #subprocess.run(['wmctrl', '-xa', 'jetbrains-rider.jetbrains-rider'], stdout=subprocess.PIPE)

if __name__=="__main__":
    main()
