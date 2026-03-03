import tkinter as tk
import random

class App(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
        self.meter = "-"
        self.create_widgets()

    def create_widgets(self):
        # initialize
        self.title_label = tk.Label(self, text="LOVE IS IN THE AIR (not)",\
                                    font=("Arial", 20, "bold"))

        self.batman = tk.Frame(self)
        self.lbl_person_1 = tk.Label(self.batman, text="First victim?")
        self.lbl_person_2 = tk.Label(self.batman, text="Second victim?")
        self.name_1 = tk.StringVar()
        self.name_2 = tk.StringVar()
        self.inp_person_1 = tk.Entry(self.batman, textvariable=self.name_1)
        self.inp_person_2 = tk.Entry(self.batman, textvariable=self.name_2)
        self.btn_match = tk.Button(self, text="MATCH!!!!!",\
                                    width=20)

        self.lbl_score =tk.Label(self,\
                                font=("Arial", 20, "bold"))

        # event bindings
        self.btn_match.bind("<Button-1>", self.match)

        # pack
        self.title_label.pack(pady=10)

        self.batman.pack()
        self.lbl_person_1.grid(row=0, column=0)
        self.lbl_person_2.grid(row=0, column=1)
        self.inp_person_1.grid(row=1, column=0)
        self.inp_person_2.grid(row=1, column=1)

        self.btn_match.pack()
        self.lbl_score.pack()

    def match(self, event):
        n1 = self.name_1.get()
        n2 = self.name_2.get()
        print(n2)

        self.meter = random.randint(1, 100)
        self.lbl_score["text"] = self.meter


app = App()
app.master.title("LOVE METER AHAYYY")
app.master.geometry("400x200")

app.master.mainloop()
