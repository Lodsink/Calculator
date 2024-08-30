import tkinter as tk

# Функция для обработки нажатий кнопок
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            screen_var.set(result)
        except Exception as e:
            screen_var.set("Error")
    elif text == "C":
        screen_var.set("")
    else:
        screen_var.set(screen_var.get() + text)

# Основное окно
root = tk.Tk()
root.title("iPhone-like Calculator")

# Переменная для хранения выражения
screen_var = tk.StringVar()

# Экран калькулятора
screen = tk.Entry(root, textvar=screen_var, font="lucida 20 bold", bd=10, insertwidth=4, width=14, borderwidth=4, justify="right")
screen.grid(row=0, column=0, columnspan=4)

# Кнопки калькулятора
buttons = [
    'C', '(', ')', '/',
    '7', '8', '9', '*',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    '0', '.', '=', 
]

row = 1
col = 0

for button in buttons:
    btn = tk.Button(root, text=button, padx=20, pady=15, font="lucida 15 bold")
    btn.grid(row=row, column=col, sticky="nsew")
    btn.bind("<Button-1>", click)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

# Настройки размеров сетки
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
