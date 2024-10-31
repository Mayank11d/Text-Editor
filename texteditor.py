import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, Menu

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")
        self.root.geometry("800x600")

        # Create a toolbar
        self.toolbar = tk.Frame(root, bg='lightgrey')
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        # Add buttons to the toolbar
        self.new_button = tk.Button(self.toolbar, text="New", command=self.new_file)
        self.new_button.pack(side=tk.LEFT, padx=2, pady=2)

        self.open_button = tk.Button(self.toolbar, text="Open", command=self.open_file)
        self.open_button.pack(side=tk.LEFT, padx=2, pady=2)

        self.save_button = tk.Button(self.toolbar, text="Save", command=self.save_file)
        self.save_button.pack(side=tk.LEFT, padx=2, pady=2)

        self.toggle_dark_mode_button = tk.Button(self.toolbar, text=" Dark Mode", command=self.toggle_dark_mode)
        self.toggle_dark_mode_button.pack(side=tk.LEFT, padx=2, pady=2)

        # Text area
        self.text_area = scrolledtext.ScrolledText(root, wrap='word', font=('Arial', 12))
        self.text_area.pack(expand=True, fill='both')

        # Status bar
        self.status_bar = tk.Label(root, text="Welcome to Notepad", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Update status bar on key release
        self.text_area.bind("<KeyRelease>", self.update_status)

        # Current file name
        self.current_file = None
        self.is_dark_mode = False

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.current_file = None
        self.status_bar.config(text="New File")

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                                filetypes=[("Text files", "*.txt"),
                                                           ("All files", "*.*")])
        if file_path:
            self.text_area.delete(1.0, tk.END)
            with open(file_path, 'r') as file:
                self.text_area.insert(tk.END, file.read())
            self.current_file = file_path
            self.update_status()

    def save_file(self):
        if self.current_file:
            with open(self.current_file, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.status_bar.config(text=f"Saved: {self.current_file}")
        else:
            self.save_as()

    def save_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                   filetypes=[("Text files", "*.txt"),
                                                              ("All files", "*.*")])
        if file_path:
            self.current_file = file_path
            self.save_file()

    def toggle_dark_mode(self):
        if self.is_dark_mode:
            self.text_area.config(bg='white', fg='black')
            self.status_bar.config(bg='lightgrey', fg='black')
            self.root.config(bg='lightgrey')
            self.toggle_dark_mode_button.config(bg='lightgrey', fg='black')
            self.is_dark_mode = False
        else:
            self.text_area.config(bg='#2e2e2e', fg='white')
            self.status_bar.config(bg='#3c3c3c', fg='white')
            self.root.config(bg='#3c3c3c')
            self.toggle_dark_mode_button.config(bg='#3c3c3c', fg='white')
            self.is_dark_mode = True

        self.update_status()

    def update_status(self, event=None):
        content_length = len(self.text_area.get(1.0, tk.END)) - 1  # Exclude the last newline
        if self.current_file:
            self.status_bar.config(text=f"{self.current_file} | Characters: {content_length}")
        else:
            self.status_bar.config(text=f"New File | Characters: {content_length}")

if __name__ == "__main__":
    root = tk.Tk()
    editor = Notepad(root)
    root.mainloop()
