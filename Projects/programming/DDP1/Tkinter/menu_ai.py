import tkinter as tk
from tkinter import messagebox

def new_file():
    messagebox.showinfo("New", "Creating new file...")

def open_file():
    messagebox.showinfo("Open", "Opening file...")

def about_app():
    messagebox.showinfo("About", "Simple Tkinter Menu App\nVersion 1.0")

# Create main window
root = tk.Tk()
root.title("Simple Menu Example")
root.geometry("400x300")

# Create menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)

# File menu
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Edit menu
edit_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")

# Help menu
help_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about_app)

root.mainloop()