from tkinter import *
from tkinter import ttk

def mostrar():
    suma = (entrada.get())+ (entrada2.get())
    print(suma)
    ttk.Label(cuadrito, text=suma).grid(column=0, row=4)
    
root = Tk()
root.title("titulo de la ventana")
root.geometry("720x480")
cuadrito = ttk.Frame(root, padding=10)
cuadrito.grid(padx=12, pady=12)

ttk.Label(cuadrito, text="Hello World!").grid(column=0, row=0, padx=12, pady=12)
entrada = ttk.Entry(cuadrito)
entrada2 = ttk.Entry(cuadrito)

entrada.grid(column=0, row=0)
entrada2.grid(column=0, row=1)

print(entrada)

ttk.Button(cuadrito, text="Imprimir", command=mostrar).grid(column=0, row=2)

root.mainloop()


