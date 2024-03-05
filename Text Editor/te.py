import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Text Editor")
        self.textarea = tk.Text(self.master, wrap="word", undo=True)
        self.textarea.pack(expand=True, fill="both")
        self.setup_menu()

    def setup_menu(self):
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=False)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        edit_menu = tk.Menu(menubar, tearoff=False)
        edit_menu.add_command(label="Undo", command=self.textarea.edit_undo)
        edit_menu.add_command(label="Redo", command=self.textarea.edit_redo)
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=self.cut_text)
        edit_menu.add_command(label="Copy", command=self.copy_text)
        edit_menu.add_command(label="Paste", command=self.paste_text)
        edit_menu.add_separator()
        edit_menu.add_command(label="Select All", command=self.select_all)
        menubar.add_cascade(label="Edit", menu=edit_menu)

        format_menu = tk.Menu(menubar, tearoff=False)
        format_menu.add_command(label="Bold", command=self.bold_text)
        format_menu.add_command(label="Italic", command=self.italic_text)
        menubar.add_cascade(label="Format", menu=format_menu)

    def new_file(self):
        self.textarea.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                self.textarea.delete(1.0, tk.END)
                self.textarea.insert(1.0, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.textarea.get(1.0, tk.END))

    def cut_text(self):
        self.textarea.event_generate("<<Cut>>")

    def copy_text(self):
        self.textarea.event_generate("<<Copy>>")

    def paste_text(self):
        self.textarea.event_generate("<<Paste>>")

    def select_all(self):
        self.textarea.tag_add("sel", "1.0", "end")

    def bold_text(self):
        self.textarea.tag_configure("bold", font=("Arial", 12, "bold"))
        if "bold" in self.textarea.tag_names("sel.first"):
            self.textarea.tag_remove("bold", "sel.first", "sel.last")
        else:
            self.textarea.tag_add("bold", "sel.first", "sel.last")

    def italic_text(self):
        self.textarea.tag_configure("italic", font=("Arial", 12, "italic"))
        if "italic" in self.textarea.tag_names("sel.first"):
            self.textarea.tag_remove("italic", "sel.first", "sel.last")
        else:
            self.textarea.tag_add("italic", "sel.first", "sel.last")

def main():
    root = tk.Tk()
    text_editor = TextEditor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
