import tkinter as tk
from tkinter import filedialog
import os
# Create the main window
window = tk.Tk()
def open_path():
    path = filedialog.askopenfilename()
    entry_path.insert(0, path)
# Create a label to display the path
label_path = tk.Label(window, text="Path: ")

# Create an entry box to enter the path
entry_path = tk.Entry(window)

# Create a button to open the file dialog
button_open = tk.Button(window, text="Open", command=open_path)

# Create a label to display the search results
label_results = tk.Label(window, text="Results: ")

# Create a text box to display the search results
text_results = tk.Text(window)

# Create a textarea to display the file content
textarea = tk.Text(window)

# Place the widgets on the window
label_path.grid(row=0, column=0)
entry_path.grid(row=0, column=1)
button_open.grid(row=0, column=2)
label_results.grid(row=1, column=0)
text_results.grid(row=1, column=1)
textarea.grid(row=2, column=0, columnspan=2)

# Bind the open button to the open_path function
button_open.bind("<Button-1>", open_path)

# Start the main loop
window.mainloop()

# This function opens the file dialog and gets the path of the selected file


# This function searches the specified path for the given string and displays the results in the text box
def search_files(path, string):
    for root, dirs, files in os.walk(path):
        for file in files:
            if string in file:
                text_results.insert(tk.END, os.path.join(root, file) + "\n")

# This function opens the file and displays the content in the textarea
def open_file():
    path = entry_path.get()
    with open(path, "r") as f:
        content = f.read()
        textarea.insert(tk.END, content)

# Bind the open file button to the open_file function
button_open_file = tk.Button(window, text="Open File", command=open_file)
button_open_file.grid(row=3, column=0, columnspan=2)
