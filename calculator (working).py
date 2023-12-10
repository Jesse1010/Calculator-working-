import tkinter as tk
from tkinter import messagebox
import webbrowser

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jesse's Calculator")

        self.entry = tk.Entry(root, width=16, font=('Arial', 20), bd=5, insertwidth=4, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('0', 1, 1), ('1', 1, 2), ('2', 1, 3),
            ('3', 2, 1), ('4', 2, 2), ('5', 2, 3),
            ('6', 3, 1), ('7', 3, 2), ('8', 3, 3),
            ('9', 4, 1), ('C', 4, 2), ('=', 4, 3),
            ('/', 1, 0), ('*', 2, 0), ('-', 3, 0), ('+', 4, 0),
        ]

        for (text, row, column) in buttons:
            padx_value = 10 if text.isdigit() or text in {'C', '='} else 20
            pady_value = 10 if text.isdigit() or text in {'C', '='} else 20
            button = tk.Button(root, text=text, padx=padx_value, pady=pady_value, font=('Arial', 16), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column, sticky=tk.NSEW)

        exit_button = tk.Button(root, text="Exit", padx=5, pady=5, font=('Arial', 10), bg='red', fg='white', command=self.on_exit_click)
        exit_button.grid(row=5, column=0, columnspan=4, sticky=tk.NSEW)

        more_projects_button = tk.Button(root, text="More Projects", padx=5, pady=5, font=('Arial', 10), command=self.open_more_projects)
        more_projects_button.grid(row=5, column=0, sticky=tk.SW)

        # button space config (makes it look nice)
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, text):
        current_text = self.entry.get()

        if text == 'C':
            self.entry.delete(0, tk.END)
        elif text == '=':
            try:
                result = eval(current_text)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, text)
#ekit button and project link
            
    def on_exit_click(self):
        if messagebox.askokcancel("Exit", "Would you like to exit?"):
            self.root.destroy()

    def open_more_projects(self):
        webbrowser.open("https://github.com/Jesse1010")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
