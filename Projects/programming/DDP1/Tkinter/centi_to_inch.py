import tkinter as tk
from tkinter import ttk

# i should just focus
class MyGUI():
    def __init__(self, master):
        self.master = master

        # Window configs
        self.master.title("WHAT THE FUCK IS A CENTIMETER 🦅🦅🦅")
        self.master.geometry("800x200")

        # Title, subtitle
        self.title_label = tk.Label(self.master, text="WHAT THE FUCK IS A CENTIMETER 🦅🦅🦅", 
                                    font=("Arial", 20, "bold"))
        self.title_label.pack()
        self.subtitle_label = tk.Label(self.master, text="Convert the 'metric' of these communists to our glorious 'inches'. FOR FREEDOOOMMMMMMM")
        self.subtitle_label.pack()

        # Input
        self.input_frame = ttk.Frame(self.master)

        self.centi_input = tk.Entry(self.input_frame, 
                                    width=20)
        self.centi_input.grid(row=0, column=0)
        self.convert_btn = tk.Button(self.input_frame, text="Convert", 
                                     command=self.convert)
        self.convert_btn.grid(row=0, column=1, padx=10)

        self.input_frame.pack(pady=10)

        # Output
        self.result_label = tk.Label(self.master, text="0 INCHES", 
                                     font=("Arial", 20, "bold"))
        self.result_label.pack(pady=10)
        # or u can use stringVar

        # Footer
        self.footer_label = tk.Label(self.master, text="PROUD TO BE AMERICAN", fg="grey")
        self.footer_label.pack(pady=10)

    def convert(self):
        try:
            centi = float(self.centi_input.get())
        except ValueError:
            result = "Enter a valid number, communist!!"
        else:
            CENTI_TO_INCH_RATIO = 0.393701
            result = float(centi) * CENTI_TO_INCH_RATIO
            result = round(result, 2)
        self.result_label.config(text=str(result) + ' INCHES**')


root = tk.Tk()
MyGUI(root)
root.mainloop()