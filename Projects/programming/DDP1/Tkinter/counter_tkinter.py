import tkinter as tk

class App(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
        self.number = 0
        self.create_widgets()

    def create_widgets(self):
        #
        self.title_label = tk.Label(self, text="Counter App!")
        self.number_label = tk.Label(self, text=self.number)
        self.increment_btn = tk.Button(self, text="Increment",\
                                    width=20)
        self.reset_btn = tk.Button(self, text="Reset",\
                                    width=20)

        # event bindings
        self.increment_btn.bind("<Button-1>", self.count)
        self.reset_btn.bind("<Button-1>", self.reset)

        # pack
        self.title_label.pack()
        self.number_label.pack()
        self.increment_btn.pack()
        self.reset_btn.pack()

    def count(self, event):
        self.number += 1
        self.number_label["text"] = self.number

    def reset(self, event):
        self.number = 0
        self.number_label["text"] = self.number

app = App()
app.master.title("Counter")
app.master.geometry("300x200")

app.master.mainloop()
