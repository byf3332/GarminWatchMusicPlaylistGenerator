import listCreator
import tkinter as tk
from tkinter import filedialog
from datetime import datetime

# create main window
root = tk.Tk()
root.title("GARMIN Watch Music Playlist Generator")

# fix window size to 500 x 200
fixed_width = 500
fixed_height = 200
root.geometry(f"{fixed_width}x{fixed_height}")
root.resizable(False, False)  # no resizing

# enable dpi awareness（only work on windows）
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except Exception as e:
    print(f"Error setting DPI awareness: {e}") # handle non-windows system

# initilize global variable
directory = ""

# function: browse audio file folder
def browse_folder():
    global directory
    directory = filedialog.askdirectory()
    if directory:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, directory)

# function: click button
def execute_action():
    audio_titles = listCreator.scan_directory(directory)
    sorted_titles = listCreator.sort_titles(audio_titles)
    listCreator.create_m3u8(sorted_titles, directory)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result_label.config(text=f"List stored in folder inputed!: {current_time}")
# create path entry box
path_entry = tk.Entry(root, width=50)
path_entry.grid(row=2, column=1, padx=10, pady=10)

# create select folder button
browse_button = tk.Button(root, text="Choose Folder", command=browse_folder)
browse_button.grid(row=2, column=2, padx=10, pady=10)

# create generate playlist button
execute_button = tk.Button(root, text="Create Playlist", command=execute_action)
execute_button.grid(row=3, column=1, columnspan=3, padx=10, pady=10)

# create result label
result_label = tk.Label(root, text="")
result_label.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

root.mainloop()
