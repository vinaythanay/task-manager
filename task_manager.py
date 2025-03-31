from tkinter import (
    Tk,
    Label,
    Entry,
    Button,
    Listbox,
    Scrollbar,
    END,
    Toplevel,
    messagebox,
)
import json

class Task:
    def __init__(self, title, category, details, due_date, priority):
        self.title = title
        self.category = category
        self.details = details
        self.due_date = due_date
        self.priority = priority

class TaskManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.tasks = []
        
        # Window setup
        self.setup_window()
        
        # GUI Components
        self.setup_ui_components()
        
        # Load existing tasks from file
        self.load_tasks()

        # Exit handler
        self.root.protocol("WM_DELETE_WINDOW", self.exit_application)

    def setup_window(self):
        window_width, window_height = 600, 400
        screen_width, screen_height = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def setup_ui_components(self):
        # Input fields and labels
        self.title_label = Label(self.root, text="Title:", fg="blue")
        self.title_entry = Entry(self.root)
        self.category_label = Label(self.root, text="Category:", fg="blue")
        self.category_entry = Entry(self.root)
        self.details_label = Label(self.root, text="Details:", fg="blue")
        self.details_entry = Entry(self.root)
        self.due_date_label = Label(self.root, text="Due Date:", fg="blue")
        self.due_date_entry = Entry(self.root)
        self.priority_label = Label(self.root, text="Priority:", fg="blue")
        self.priority_entry = Entry(self.root)

        # Task listbox and scrollbar
        self.task_listbox = Listbox(self.root, height=10)
        self.scrollbar = Scrollbar(self.root)

        # Buttons
        self.add_button = Button(self.root, text="Add Task", command=self.add_task, bg="green", fg="white")
        self.edit_button = Button(self.root, text="Edit Task", command=self.edit_task, bg="orange", fg="white")
        self.delete_button = Button(self.root, text="Delete Task", command=self.delete_task, bg="red", fg="white")
        self.view_button = Button(self.root, text="View Tasks", command=self.view_tasks, bg="blue", fg="white")
        self.save_button = Button(self.root, text="Save", command=self.save_tasks, bg="purple", fg="white")
        
        # Layout
        self.title_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)
        self.category_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.category_entry.grid(row=1, column=1, padx=5, pady=5)
        self.details_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.details_entry.grid(row=2, column=1, padx=5, pady=5)
        self.due_date_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.due_date_entry.grid(row=3, column=1, padx=5, pady=5)
        self.priority_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.priority_entry.grid(row=4, column=1, padx=5, pady=5)

        self.task_listbox.grid(row=0, column=2, rowspan=5, padx=5, pady=5, sticky="nsew")
        self.scrollbar.grid(row=0, column=3, rowspan=5, sticky="ns")

        self.add_button.grid(row=5, column=0, padx=5, pady=5)
        self.edit_button.grid(row=5, column=1, padx=5, pady=5)
        self.delete_button.grid(row=5, column=2, padx=5, pady=5)
        self.view_button.grid(row=6, column=0, padx=5, pady=5)
        self.save_button.grid(row=6, column=1, padx=5, pady=5)

        # Scrollbar functionality
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

    def add_task(self):
        new_task_data = {
            "title": self.title_entry.get(),
            "category": self.category_entry.get(),
            "details": self.details_entry.get(),
            "due_date": self.due_date_entry.get(),
            "priority": self.priority_entry.get()
        }
        
        if all(new_task_data.values()):
            task = Task(**new_task_data)
            self.tasks.append(task)
            self.clear_input_fields()
            self.update_task_listbox()
        else:
            messagebox.showwarning("Input Error", "Please fill in all the fields.")

    def edit_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.tasks[selected_task_index[0]]
            self.show_edit_window(task)
        else:
            messagebox.showwarning("Selection Error", "Please select a task to edit.")

    def show_edit_window(self, task):
        edit_window = Toplevel(self.root)
        edit_window.title("Edit Task")
        
        labels = ["Title", "Category", "Details", "Due Date", "Priority"]
        entries = [
            Entry(edit_window),
            Entry(edit_window),
            Entry(edit_window),
            Entry(edit_window),
            Entry(edit_window)
        ]
        
        for idx, label in enumerate(labels):
            Label(edit_window, text=f"{label}:", fg="blue").grid(row=idx, column=0, padx=5, pady=5, sticky="w")
            entries[idx].grid(row=idx, column=1, padx=5, pady=5)
            entries[idx].insert(END, getattr(task, label.lower()))

        def update_task():
            updated_data = [entry.get() for entry in entries]
            if all(updated_data):
                task.title, task.category, task.details, task.due_date, task.priority = updated_data
                edit_window.destroy()
                self.update_task_listbox()
            else:
                messagebox.showwarning("Input Error", "All fields must be filled.")

        Button(edit_window, text="Update", command=update_task, bg="green", fg="white").grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.tasks[selected_task_index[0]]
            confirmation = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete: {task.title}?")
            if confirmation:
                self.tasks.pop(selected_task_index[0])
                self.update_task_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def view_tasks(self):
        self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, END)
        for task in self.tasks:
            task_info = f"Title: {task.title} | Category: {task.category} | Due: {task.due_date} | Priority: {task.priority}"
            self.task_listbox.insert(END, task_info)

    def clear_input_fields(self):
        self.title_entry.delete(0, END)
        self.category_entry.delete(0, END)
        self.details_entry.delete(0, END)
        self.due_date_entry.delete(0, END)
        self.priority_entry.delete(0, END)

    def save_tasks(self):
        try:
            with open("tasks.json", "w") as file:
                task_data = [{"title": task.title, "category": task.category, "details": task.details, "due_date": task.due_date, "priority": task.priority} for task in self.tasks]
                json.dump(task_data, file)
            messagebox.showinfo("Save Successful", "Tasks saved successfully.")
        except IOError:
            messagebox.showerror("File Error", "Error while saving tasks.")

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                task_data = json.load(file)
                for task_info in task_data:
                    task = Task(**task_info)
                    self.tasks.append(task)
                self.update_task_listbox()
        except IOError:
            messagebox.showwarning("File Error", "No saved tasks found, starting fresh.")

    def exit_application(self):
        self.save_tasks()
        self.root.quit()


root = Tk()
task_manager = TaskManagerGUI(root)
root.mainloop()
