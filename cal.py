import tkinter as tk

def on_click(button_text):
    current_text = entry.get()

    if button_text == "=":
        try:
            result = str(eval(current_text))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)


root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, pady=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

frame = tk.Frame(root)
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill="both")
    for button in row:
        b = tk.Button(
            row_frame,
            text=button,
            font=("Arial", 18),
            command=lambda val=button: on_click(val)
        )
        b.pack(side="left", expand=True, fill="both", padx=5, pady=5)

root.mainloop()
