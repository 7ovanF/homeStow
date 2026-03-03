import tkinter as tk
from tkinter import ttk, messagebox

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.create_menu()
        self.create_widgets()
        self.pack_widgets()

        self.pack()

    def create_menu(self):
        self.menubar = tk.Menu(self.master)
        self.master.config(menu=self.menubar)

        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(
            label="Do A",
            command=self.invoke
        )

        self.edit_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(
            label="Do B",
            command=self.invoke
        )

    def create_widgets(self):
        self.btn = ttk.Button(self, text="A Button", command=self.invoke, state="disabled")
        self.lbl = ttk.Label(self, text="Hello, World!")

        self.cnv = tk.Canvas(self)
        self.cnv.config(bg="blue", width=200, height=150)
        self.cnv.create_line(0, 0, 100, 50, fill="red")

        self.checked = tk.StringVar(value="42")
        self.check = ttk.Checkbutton(self, text="A Checkbutton", variable=self.checked, \
            onvalue="42", offvalue="Fuck you")

        # self.password = tk.StringVar()
        self.ent = ttk.Entry(self, show="*", text="",\
            width=8)
        self.ent.bind("<Return>", self.invoke)
        
        self.config(relief="raised", borderwidth=15)

        self.menu = tk.Menu(self)
        self.menu_btn = ttk.Menubutton(self.menu)
        self.msg = tk.Message(self)
        self.radio = ttk.Radiobutton(self)
        self.txt = tk.Text(self)

    def invoke(self, event=None):
        self.check.invoke()
        self.ent.config(text="brawdoak")
        self.ent.insert(2, "bruh man")
        self.ent.delete(4, 7)
        self.ent.icursor(2)

        messagebox.showinfo(message=f"bros password isnt {self.checked.get()} lmao")

    def pack_widgets(self):
        self.btn.pack()
        self.lbl.pack()
        self.cnv.pack()
        self.check.pack()
        self.ent.pack()
        # self.menu.pack()
        # self.menu_btn.pack()
        self.msg.pack()
        self.radio.pack()
        self.txt.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(master=root)
    root.geometry("800x600")
    root.mainloop()