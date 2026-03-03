import tkinter as tk
from tkinter import ttk, messagebox

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Todo List')
        self.geometry('800x600')

        self.todo_page = TodoPage(self)
        self.todo_page.pack(fill='both', expand=True)

        self.mainloop()

# Discontinued bc fuck it, why would i learn tkinter extensively
class TodoPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.tasks = []

        self.init_widgets()
        self.pack_widgets()

        # DEV: To show true size
        self.config(bg="blue")
        
    def init_widgets(self):
        self.title_label = ttk.Label(self, text="Todo", font=("Arial", 30, "bold"))
        
        # New task input
        self.ntask_frame = ttk.Frame(self)
        self.ntask_name = tk.StringVar()
        self.ntask_input = ttk.Entry(self.ntask_frame, textvariable=self.ntask_name)
        self.ntask_input.bind("<Return>", self.add_task)
        self.ntask_btn = ttk.Button(self.ntask_frame, text="Add", \
            width="50px")
        self.ntask_btn.bind("<ButtonRelease>", self.add_task)

        # List
        self.task_list = tk.StringVar(value=self.tasks)
        self.listbox = tk.Listbox(self, listvariable=self.task_list)

    def pack_widgets(self):
        self.title_label.pack(pady=10, padx=20)

        self.ntask_frame.pack()
        self.ntask_input.grid(column=0, row=0)
        self.ntask_btn.grid(column=1, row=0)

        self.listbox.pack()

    def add_task(self, event):
        name = self.ntask_name.get().strip()
        if not name:
            messagebox.showwarning(message="No task name.")
            return

        self.tasks += [name]
        self.task_list.set(self.tasks)
        print(f"added {name}") # DEV: remove
        self.ntask_name.set("")

if __name__ == "__main__":
    app = App()