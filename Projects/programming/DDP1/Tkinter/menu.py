import tkinter as tk

# class MenuBar(tk.Menu):
#     def __init__(self, master=None):
#         super().__init__(master)

#         self.file_menu = tk.Menu(self, tearoff=0)
#         self.add_cascade(label="File", menu=self.file_menu)
#         self.file_menu.add_command(
#             label='Do something',
#         )
#         self.file_menu.add_separator()
#         self.file_menu.add_command(
#             label='Exit',
#             command=self.destroy
#         )

#         self.create_widgets()

#     def create_widgets(self):
#         self.lbl = tk.Label(self, text="Highway to Hail")
#         self.lbl.pack()

# if __name__ == "__main__":
#     root = tk.Tk()
#     menu = MenuBar(master=root)
#     root.config(menu=menu)
#     root.geometry("800x600")
#     root.mainloop()

# No structure
root = tk.Tk()
menubar = tk.Menu(master=root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(
    label="Do something"
)

root.mainloop()