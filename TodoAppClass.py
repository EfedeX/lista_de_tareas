import tkinter as tk
from tkinter import ttk, messagebox


class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("My to-do app")
        self.geometry("800x600")
        self.minsize(300, 400)

        self.tasks = []
        self.create_widgets()
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

    def create_widgets(self):
        self.task_entry = ttk.Entry(self, font=("Arial", 12))
        self.task_entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        add_button = ttk.Button(self, text="Add Task", command=self.add_task)
        add_button.grid(row=0, column=1, padx=5, pady=5)

        self.task_list = tk.Listbox(self, font=("Arial", 12), selectmode=tk.SINGLE)
        self.task_list.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.task_list.yview)
        scrollbar.grid(row=1, column=2, sticky="ns")
        self.task_list.configure(yscrollcommand=scrollbar.set)

        button_frame = ttk.Frame(self)
        button_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        complete_button = ttk.Button(button_frame, text="Toogle completion", command=self.complete_task)
        complete_button.pack(side="left", padx=5)

        delete_button = ttk.Button(button_frame, text="Delete Task", command=self.delete_task)
        delete_button.pack(side="left", padx=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Invalid Input", "Please enter a task.")

    def complete_task(self):
        try:
            index = self.task_list.curselection()[0]
            task = self.task_list.get(index)
            if task.startswith("✓ "):
                new_task = task[2:]
            else:
                new_task = f"✓ {task}"
            self.task_list.delete(index)
            self.task_list.insert(index, new_task)
        except IndexError:
            messagebox.showwarning("No Task Selected", "Please select a task to mark as complete.")

    def delete_task(self):
        try:
            index = self.task_list.curselection()[0]
            self.task_list.delete(index)
            del self.tasks[index]
        except IndexError:
            messagebox.showwarning("No Task Selected", "Please select a task to delete.")