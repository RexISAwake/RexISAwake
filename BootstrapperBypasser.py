print('''                                     

 
 ▀█████████▄  ▄██   ▄    ▄███████▄    ▄████████    ▄████████    ▄████████    ▄████████    ▄████████ 
 ███    ███ ███   ██▄   ███    ███   ███    ███   ███    ███   ███    ███   ███    ███   ███    ███ 
  ███    ███ ███▄▄▄███   ███    ███   ███    ███   ███    █▀    ███    █▀    ███    █▀    ███    ███ 
 ▄███▄▄▄██▀  ▀▀▀▀▀▀███   ███    ███   ███    ███   ███          ███         ▄███▄▄▄      ▄███▄▄▄▄██▀ 
▀▀███▀▀▀██▄  ▄██   ███ ▀█████████▀  ▀███████████ ▀███████████ ▀███████████ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
  ███    ██▄ ███   ███   ███          ███    ███          ███          ███   ███    █▄  ▀███████████ 
  ███    ███ ███   ███   ███          ███    ███    ▄█    ███    ▄█    ███   ███    ███   ███    ███ 
▄█████████▀   ▀█████▀   ▄████▀        ███    █▀   ▄████████▀   ▄████████▀    ██████████   ███    ███ 
__     _______ 
\ \   / /___  |
 \ \ / /   / /                         
  \ V /   / /  
   \_/   /_/                                       
''')

input("Press enter to open Bypasser...")
print("- Steam is sadly not supported")
print("- New Bootstrapper")
print("- Using Python!")

import tkinter as tk
from tkinter import filedialog
import os
import subprocess

def run_file():
    file_path = filedialog.askopenfilename()
    os.system(f'cmd /min /C "set __COMPAT_LAYER=RUNASINVOKER && start "" "{file_path}"')

def drag_window(event):
    x = root.winfo_x() + event.x
    y = root.winfo_y() + event.y
    root.geometry(f'+{x}+{y}')

def close_window():
    root.destroy()

def minimize_window():
    root.iconify()

root = tk.Tk()
root.title("Bypasser V7")
root.attributes("-topmost", True)
root.resizable(False, False)

root.overrideredirect(True)

frame = tk.Frame(root, width=200, height=100, bg='black')
frame.pack(padx=5, pady=5)

label = tk.Label(frame, text="Bypasser V7", font=("Arial", 15), fg='white', bg='black')
label.pack(pady=5)

button = tk.Button(frame, text="Browse", command=run_file, fg='white', bg='black')
button.pack(pady=5)

close_button = tk.Button(frame, text="X", command=close_window, fg='red', bg='black')
close_button.pack(side=tk.RIGHT, anchor=tk.NE)

[]
small_label = tk.Label(frame, text="Steam Not Supported", font=("Arial", 8), fg='gray', bg='black')
small_label.pack(side=tk.LEFT, anchor=tk.SW)

frame.bind("<B1-Motion>", drag_window)

root.mainloop()
# //WinAPI0.1//Bootstrapper//.exe
# find local "WindAPI0.1"
#  Auto Update API
"//WinAPI0.1//Bootstrapper//.exe"
# ________________________________________________________________________
    # inject_file(file_path):
    # inject file using CopyFiler and WinAPI
    # this is a simplified example, you may need to use more advanced techniques
    # to inject the file successfully
    # if you want the api take it this is a low quality made api so yeah
    # Not steam supported if you want steam i need me some money!
# ________________________________________________________________________
