import tkinter as tk

class ToDoListApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List")
        self.geometry("300x400")

        self.entry_task = tk.Entry(self)
        self.entry_task.pack(pady=10)

        self.button_add = tk.Button(self, text="Add Task", command=self.add_task)
        self.button_add.pack()

        self.button_delete = tk.Button(self, text="Delete Task", command=self.delete_task)
        self.button_delete.pack(pady=5)

        self.button_complete = tk.Button(self, text="Mark as Completed", command=self.mark_completed)
        self.button_complete.pack(pady=5)

        self.listbox = tk.Listbox(self, selectmode=tk.SINGLE)
        self.listbox.pack(fill=tk.BOTH, expand=True)

    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.listbox.insert(tk.END, task)
            self.entry_task.delete(0, tk.END)

    def delete_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            self.listbox.delete(selected_index[0])

    def mark_completed(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            task = self.listbox.get(selected_index[0])
            self.listbox.delete(selected_index[0])
            self.listbox.insert(tk.END,  "✔️  "+ task )

if __name__ == "__main__":
    app = ToDoListApp()
    app.mainloop()