import tkinter as tk

def on_button_click(value):
    current = display.get()
    if value == "=":
        try:
            result = str(eval(current))
            display.set(result)
        except Exception:
            display.set("Error")
    elif value == "C":
        display.set("")
    elif value == "±":
        if current and current[0] == "-":
            display.set(current[1:])
        else:
            display.set("-" + current)
    else:
        display.set(current + value)


root = tk.Tk()
root.title("🌈 Modern Calculator")
root.geometry("400x600")
root.configure(bg="#2b2b2b")  

display = tk.StringVar()


entry = tk.Entry(
    root, 
    textvariable=display, 
    font=("Helvetica", 36), 
    bg="#1e1e1e", 
    fg="white", 
    bd=0, 
    justify="right", 
    relief="flat"
)
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=20, pady=30, ipady=20)


button_cfg = {
    "font": ("Helvetica", 22),
    "bd": 0,
    "relief": "flat",
    "height": 2,
    "width": 5,
    "activebackground": "#555",
    "activeforeground": "white",
}


buttons = [
    ("C", 1, 0, "#ff3b30"), ("±", 1, 1, "#ffcc00"), ("%", 1, 2, "#ffcc00"), ("/", 1, 3, "#ff9500"),
    ("7", 2, 0, "#3a3a3a"), ("8", 2, 1, "#3a3a3a"), ("9", 2, 2, "#3a3a3a"), ("*", 2, 3, "#ff9500"),
    ("4", 3, 0, "#3a3a3a"), ("5", 3, 1, "#3a3a3a"), ("6", 3, 2, "#3a3a3a"), ("-", 3, 3, "#ff9500"),
    ("1", 4, 0, "#3a3a3a"), ("2", 4, 1, "#3a3a3a"), ("3", 4, 2, "#3a3a3a"), ("+", 4, 3, "#ff9500"),
    ("0", 5, 0, "#3a3a3a"), (".", 5, 1, "#3a3a3a"), ("=", 5, 2, "#34c759"),
]


for (text, row, col, color) in buttons:
    button = tk.Button(
        root, 
        text=text, 
        bg=color, 
        fg="white",
        command=lambda value=text: on_button_click(value),
        **button_cfg
    )
    button.grid(row=row, column=col, sticky="nsew", padx=8, pady=8)


zero_button = tk.Button(
    root,
    text="0",
    bg="#3a3a3a",
    fg="white",
    command=lambda value="0": on_button_click(value),
    **button_cfg
)
zero_button.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=8, pady=8)


for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
