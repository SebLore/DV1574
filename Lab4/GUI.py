'''
This is a simple text editor that uses CustomTkinter to create a GUI.
The text editor has a menu bar with options to open and save files.
'''

import customtkinter as ctk
from tkinter import filedialog


def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            text_editor.delete(1.0, ctk.END)
            text_editor.insert(ctk.END, file.read())


def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt", filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_editor.get(1.0, ctk.END))


def create_app():
    app = ctk.CTk()
    app.title("CustomTkinter Text Editor")
    app.geometry("800x600")

    global text_editor
    text_editor = ctk.CTkTextbox(app, wrap="word")
    text_editor.pack(expand=True, fill="both")

    menu_bar = ctk.CTkMenu(app)
    file_menu = ctk.CTkMenu(menu_bar, tearoff=0)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Save", command=save_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=app.quit)
    menu_bar.add_cascade(label="File", menu=file_menu)

    app.config(menu=menu_bar)
    return app


def main():
    app = create_app()
    app.mainloop()


if __name__ == "__main__":
    main()
