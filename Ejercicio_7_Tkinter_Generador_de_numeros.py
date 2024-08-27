#Ejercicio 2.3 Generador de números
from tkinter import *
import random

def Generar():
    num1_valor = int(num1.get())
    num2_valor = int(num2.get())

    if num1_valor > num2_valor:
        num1_valor, num2_valor = num2_valor, num1_valor

    numero_generado = random.randint(num1_valor, num2_valor)
    
    entry.config(state='normal')
    entry.delete(0, END)
    entry.insert(0, str(numero_generado))
    entry.config(state='readonly')

#ventana
ventana = Tk()
ventana.title("Generador de Números")
ventana.geometry("600x300")
ventana.configure(bg="#729185")
ventana.resizable(False, False)

#marco
marco= LabelFrame(ventana, text="Generador de números", bg="#E8C39A",fg="#703111", font= ('Times New Roman',12,'bold'))
marco.place(x=30, y= 40, width=535, height=225)


#Elecciones
num1 = Spinbox(ventana, from_=1, to=100, bg="white")
num1.place(x=300, y=80, width=130, height=20)
num2 = Spinbox(ventana, from_=1, to=100, bg="white")
num2.place(x=300, y=120, width=130, height=20)


#Entrada
entry= Entry (ventana,textvariable="0", bg="#DFD3C9", state='readonly')
entry.place(x=300, y= 170, width=130, height=20)
entry.config(state='normal')
entry.insert(0,"0")
entry.config(state='readonly')

#Botón
button=Button(ventana,text="Generar",borderwidth=2, height=1, width=7,anchor="center",bg="#Cf792E", font= ('Comic sens MC',8,'bold'), command=Generar)
button.place(x=250, y=220)

# Etiquetas
label = Label(ventana, text="Primer número:", bg="#E8C39A", fg="#6b3215", font=('Impact', 12))
label.place(x=150, y=80, width=140, height=20)

label2 = Label(ventana, text="Segundo número:", bg="#E8C39A", fg="#6b3215", font=('Impact', 12))
label2.place(x=150, y=120, width=140, height=20)

label_res = Label(ventana, text="Número generado:", bg="#E8C39A", fg="#9F4619", font=('Impact', 12))
label_res.place(x=150, y=170, width=140, height=20)

ventana.mainloop()