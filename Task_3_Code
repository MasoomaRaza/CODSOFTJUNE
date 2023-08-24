import tkinter as tk

def button_click(event):
    current_text = result_label.cget("text")
    clicked_button = event.widget.cget("text")

    if clicked_button == "=":
        try:
            result = eval(current_text)
            result_label.config(text=result)
        except:
            result_label.config(text="Error")
    elif clicked_button == "C":
        result_label.config(text="")
    else:
        result_label.config(text=current_text + clicked_button)

root = tk.Tk()
root.title("Calculator")

result_label = tk.Label(root, text="", anchor="e", font=("Arial", 24))
result_label.pack(fill=tk.BOTH, expand=True)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("+", 3, 3),
    ("C", 4, 0)
]

for button_text, row, col in buttons:
    button = tk.Button(button_frame, text=button_text, font=("Arial", 18), padx=20, pady=20)
    button.grid(row=row, column=col)
    button.bind("<Button-1>", button_click)

root.mainloop()
