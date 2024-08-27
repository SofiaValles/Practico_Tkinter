#Ejercicio 2.1 Calculadora
from tkinter import *

def Validar_entrada(char):
    if char.isdigit() or char == ".":
        return True
    return False

# Cálculos
def Suma():
    try:
        num1 = float(entry.get()) if entry.get() else 0
        num2 = float(entry2.get()) if entry2.get() else 0
        suma = num1 + num2
        entry_res.config(state='normal')
        entry_res.delete(0, END)
        entry_res.insert(0, str(suma))
        entry_res.config(state='readonly')
    except ValueError:
        entry_res.config(state='normal')
        entry_res.delete(0, END)
        entry_res.insert(0, "Error")
        entry_res.config(state='readonly')

def Resta():
    try:
        num1 = float(entry.get()) if entry.get() else 0
        num2 = float(entry2.get()) if entry2.get() else 0
        resta = num1 - num2
        entry_res.config(state='normal')
        entry_res.delete(0, END)
        entry_res.insert(0, str(resta))
        entry_res.config(state='readonly')
    except ValueError:
        entry_res.config(state='normal')
        entry_res.delete(0, END)
        entry_res.insert(0, "Error")
        entry_res.config(state='readonly')

def Multiplicacion():
    try:
        num1 = float(entry.get()) if entry.get() else 0
        num2 = float(entry2.get()) if entry2.get() else 0
        multi = num1 * num2
        entry_res.config(state='normal')
        entry_res.delete(0, END)
        entry_res.insert(0, str(multi))
        entry_res.config(state='readonly')
    except ValueError:
        entry_res.config(state='normal')
        entry_res.delete(0, END)
        entry_res.insert(0, "Error")
        entry_res.config(state='readonly')

def Division():
    try:
        num1 = float(entry.get()) if entry.get() else 0
        num2 = float(entry2.get()) if entry2.get() else 0
        if num2 != 0:
            divi = num1 / num2
        else:
            divi = "Error"
        entry_res.config(state='normal')
        entry_res.delete(0, END)
        entry_res.insert(0, str(divi))
        entry_res.config(state='readonly')
    except ValueError:
        entry_res.config(state='normal')
        entry_res.delete(0, END)
        entry_res.insert(0, "Error")
        entry_res.config(state='readonly')

def Porcentaje():
    try:
        num1 = float(entry.get()) if entry.get() else 0
        num2 = float(entry2.get()) if entry2.get() else 0
        porc = (num1 * num2) / 100
        entry_res.config(state='normal')
        entry_res.delete(0, END)
        entry_res.insert(0, str(porc))
        entry_res.config(state='readonly')
    except ValueError:
        entry_res.config(state='normal')
        entry_res.delete(0, END)
        entry_res.insert(0, "Error")
        entry_res.config(state='readonly')

def Clear():
    entry.delete(0, END)
    entry2.delete(0, END)
    entry_res.config(state='normal')
    entry_res.delete(0, END)
    entry_res.config(state='readonly')

#ventana
ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("360x400")
ventana.configure(bg="#f5eb9d")
ventana.resizable(False, False)

validate_cmd = ventana.register(Validar_entrada)

# Entradas
entry = Entry(ventana, bg="white", validate="key", validatecommand=(validate_cmd, '%S'))
entry.place(x=200, y=10, width=130, height=20)

entry2 = Entry(ventana, bg="white", validate="key", validatecommand=(validate_cmd, '%S'))
entry2.place(x=200, y=60, width=130, height=20)

entry_res = Entry(ventana, bg="white", state='readonly')
entry_res.place(x=200, y=110, width=130, height=20)

#Botones
button = Button(ventana, text="+", borderwidth=2, height=4, width=10, anchor="center", bg="#affad7", font=('Comic sens MC', 11, 'bold'), command=Suma)
button.place(x=30, y=160)

button_menos = Button(ventana, text="-", borderwidth=2, height=4, width=10, anchor="center", bg="#affad7", font=('Comic sens MC', 11, 'bold'), command=Resta)
button_menos.place(x=130, y=160)

button_mult = Button(ventana, text="*", borderwidth=2, height=4, width=10, anchor="center", bg="#affad7", font=('Comic sens MC', 11, 'bold'), command=Multiplicacion)
button_mult.place(x=30, y=250)

button_div = Button(ventana, text="/", borderwidth=2, height=4, width=10, anchor="center", bg="#affad7", font=('Comic sens MC', 11, 'bold'), command=Division)
button_div.place(x=130, y=250)

button_por = Button(ventana, text="%", borderwidth=2, height=4, width=10, anchor="center", bg="#affad7", font=('Comic sens MC', 11, 'bold'), command=Porcentaje)
button_por.place(x=230, y=250)

button_clear = Button(ventana, text="Clear", borderwidth=2, height=4, width=10, anchor="center", bg="#affad7", font=('Comic sens MC', 11, 'bold'), command=Clear)
button_clear.place(x=230, y=160)

# Etiquetas
label = Label(ventana, text="Primer número", bg="#fcf8d4", fg="#785330", font=('Calibri', 12))
label.place(x=20, y=10, width=120, height=20)

label2 = Label(ventana, text="Segundo número", bg="#fcf8d4", fg="#785330", font=('Calibri', 12))
label2.place(x=20, y=60, width=140, height=20)

label_res = Label(ventana, text="Resultado", bg="#fcf8d4", fg="#785330", font=('Calibri', 12))
label_res.place(x=20, y=110, width=100, height=20)

ventana.mainloop()
