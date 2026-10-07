import tkinter as tk

def calculate(value):
    if value == "=":
        
        try:
            result = eval(screen.get())
            screen.delete(0,tk.END)
            screen.insert(0,result)
        except:
            screen.delete(0,tk.END)
            screen.insert(0,"ERROR")

    elif value == "C":
        screen.delete(0,tk.END)

    else:
        screen.insert(tk.END, value)



# MAIN CALCULTOR WINDOW

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")


# CALCULATOR DISPLAY
screen = tk.Entry(root,font=("Arial",25), justify="right")

# KEPT DISPLAY IN CALCULATOR'S WINDOW
screen.pack(fill="x", padx=10, pady=10)

# DISPLAY BUTTONS
buttons = [
        "7 8 9 /",
        "4 5 6 *",
        "1 2 3 -",
        "0 . % +",
        "C ="
        ]
for row in buttons:
    frame = tk.Frame(root)
    frame.pack()

    for btn in row.split():
        tk.Button(
                frame,
                text = btn,
                font=("Arial",18),
                width=5,
                height=2,
                command=lambda x=btn: calculate(x)
                ).pack(side="left")

root.mainloop()
