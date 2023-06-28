import tkinter as tk

def handle_mouse_click(event):
    if entry_box.collidepoint(event.x, event.y):
        canvas.focus_set()  # Define o foco no canvas para que o texto digitado seja direcionado para ele

def handle_keypress(event):
    if event.keysym == "BackSpace":
        entry_text.set(entry_text.get()[:-1])  # Remove o último caractere do texto
    elif event.char.isprintable():
        entry_text.set(entry_text.get() + event.char)  # Adiciona o caractere digitado ao texto

root = tk.Tk()

canvas = tk.Canvas(root, width=300, height=50, bg='white')
canvas.pack()

entry_box = canvas.create_rectangle(10, 10, 290, 40, outline='black')
entry_text = tk.StringVar()
entry_label = canvas.create_text(20, 25, anchor='w', textvariable=entry_text)

canvas.bind("<Button-1>", handle_mouse_click)
canvas.bind("<Key>", handle_keypress)
canvas.focus_set()  # Define o foco no canvas para que ele possa receber eventos de teclado

root.mainloop()
