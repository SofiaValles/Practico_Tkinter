#Ejercicio 2.4 Calculadora 2.
from tkinter import *

def Validar_entrada(char):
    if char.isdigit() or char == ".":
        return True
    return False

def Calcular():
    try:
        # Obtención de los valores ingresados por el usuario
        num1 = float(entry.get()) if entry.get() else 0
        num2 = float(entry2.get()) if entry2.get() else 0
        
        # Verificación de la operación seleccionada
        operacion = operacion_var.get()
        
        # Inicialización de la variable para el resultado
        resultado = "Error"
        
        # Realización de la operación correspondiente
        if operacion == 1:
            resultado = num1 + num2
        elif operacion == 2:
            resultado = num1 - num2
        elif operacion == 3:
            resultado = num1 * num2
        elif operacion == 4:
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "División por 0"

        # Actualización del campo de resultado
        entry_res.config(state='normal')
        entry_res.delete(0, END)
        entry_res.insert(0, str(resultado))
        entry_res.config(state='readonly')

    except ValueError:
        # Manejo de errores de conversión
        entry_res.config(state='normal')
        entry_res.delete(0, END)
        entry_res.insert(0, "Error")
        entry_res.config(state='readonly')

# Ventana principal
ventana = Tk()
ventana.title("Calculadora 2")
ventana.geometry("660x280")
ventana.configure(bg="#F2D5E8")
ventana.resizable(False, False)

validate_cmd = ventana.register(Validar_entrada)

# Entradas de valores
entry = Entry(ventana, bg="white", validate="key", validatecommand=(validate_cmd, '%S'))
entry.place(x=200, y=10, width=130, height=20)

entry2 = Entry(ventana, bg="white", validate="key", validatecommand=(validate_cmd, '%S'))
entry2.place(x=200, y=60, width=130, height=20)

entry_res = Entry(ventana, bg="#C1C9D9", state='readonly')
entry_res.place(x=200, y=110, width=130, height=20)

# Variable
operacion_var = IntVar()

# RadioButtons 
button_suma = Radiobutton(ventana, text="Sumar", variable=operacion_var, value=1, borderwidth=2, height=2, width=8, bg="#C1C9D9", font=('Comic sens MC', 8, 'bold'))
button_suma.place(x=500, y=50)

button_rest = Radiobutton(ventana, text="Restar", variable=operacion_var, value=2, borderwidth=2, height=2, width=8, bg="#C1C9D9", font=('Comic sens MC', 8, 'bold'))
button_rest.place(x=500, y=100)

button_mult = Radiobutton(ventana, text="Multiplicar", variable=operacion_var, value=3, borderwidth=2, height=2, width=8, bg="#C1C9D9", font=('Comic sens MC', 8, 'bold'))
button_mult.place(x=500, y=150)

button_div = Radiobutton(ventana, text="Dividir", variable=operacion_var, value=4, borderwidth=2, height=2, width=8, bg="#C1C9D9", font=('Comic sens MC', 8, 'bold'))
button_div.place(x=500, y=200)

# Botón 
button_calcular = Button(ventana, text="Calcular", borderwidth=2, height=2, width=10, bg="#F26D91", font=('Comic sens MC', 11, 'bold'), command=Calcular)
button_calcular.place(x=215, y=160)

# Etiquetas 
label = Label(ventana, text="Valor 1", bg="#F2D5E8", fg="#785330", font=('Impact', 12))
label.place(x=20, y=10, width=100, height=20)

label2 = Label(ventana, text="Valor 2", bg="#F2D5E8", fg="#785330", font=('Impact', 12))
label2.place(x=20, y=60, width=100, height=20)

label_res = Label(ventana, text="Resultado", bg="#F2D5E8", fg="#785330", font=('Impact', 12))
label_res.place(x=20, y=110, width=100, height=20)

label_op = Label(ventana, text="Operaciones", bg="#F2D5E8", fg="#A64141", font=('Impact', 16))
label_op.place(x=470, y=10, width=150, height=20)

ventana.mainloop()