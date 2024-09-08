#Juego Matemático.
from tkinter import *

def Calcular():
    try:
        # Obtención de los valores ingresados por el usuario
        num1 = float(entry.get()) if entry.get() else 0
        num2 = float(entry_2.get()) if entry_2.get() else 0
        
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



#ventana
ventana = Tk()
ventana.title("Juego Matemático")
ventana.geometry("600x450")
ventana.configure(bg="#d3dbac")
ventana.resizable(False, False)


#Entry
entry= Entry (ventana, bg="white")
entry.place(x=40, y= 70, width=100, height=20)
entry.config(state='normal')
entry.insert(0,"")
entry.config(state='readonly')

entry_2= Entry (ventana, bg="white")
entry_2.place(x=180, y= 70, width=100, height=20)
entry_2.config(state='normal')
entry_2.insert(0,"")
entry_2.config(state='readonly')

entry_res= Entry (ventana, bg="white", state='readonly')
entry_res.place(x=400, y= 200, width=170, height=20)
entry_res.config(state='normal')
entry_res.insert(0,"")
entry_res.config(state='readonly')

# Variable
operacion_var = IntVar()

#Buttons
button_resultado = Button(ventana, text="Resultado", borderwidth=2, height=1, width=10, bg="#ffbe98", font=('Comic sens MC', 10, 'bold'), command=Calcular)
button_resultado.place(x=440, y=230)

button_nuevo_num = Button(ventana, text="Nuevo Número", borderwidth=2, height=1, width=13, bg="#fbaf21", font=('Comic sens MC', 10, 'bold'), command=Calcular)
button_nuevo_num.place(x=430, y=130)

# RadioButtons 
button_suma = Radiobutton(ventana, text="Sumar", variable=operacion_var, value=1, borderwidth=2, height=2, width=8, bg="#d3dbac", font=('Comic sens MC', 8, 'bold'))
button_suma.place(x=100, y=150)

button_rest = Radiobutton(ventana, text="Restar", variable=operacion_var, value=2, borderwidth=2, height=2, width=8, bg="#d3dbac", font=('Comic sens MC', 8, 'bold'))
button_rest.place(x=100, y=200)

button_mult = Radiobutton(ventana, text="Multiplicar", variable=operacion_var, value=3, borderwidth=2, height=2, width=8, bg="#d3dbac", font=('Comic sens MC', 8, 'bold'))
button_mult.place(x=100, y=250)

button_div = Radiobutton(ventana, text="Dividir", variable=operacion_var, value=4, borderwidth=2, height=2, width=8, bg="#d3dbac", font=('Comic sens MC', 8, 'bold'))
button_div.place(x=100, y=300)

#Labels
label=Label(ventana,text="-",bg="#d3dbac",fg="#785330", font= ('Comic sens MC', 13, 'bold'))
label.place(x=153, y= 70, width=15, height=15)

label_juegos=Label(ventana,text="Juegos: ",bg="#d3dbac",fg="#785330", font= ('Comic sens MC', 8, 'bold'))
label_juegos.place(x=400, y= 300, width=50, height=35)

label_buenos=Label(ventana,text="Buenos: ",bg="#d3dbac",fg="#785330", font= ('Comic sens MC', 8, 'bold'))
label_buenos.place(x=400, y= 350, width=50, height=35)

label_malos=Label(ventana,text="Malos: ",bg="#d3dbac",fg="#785330", font= ('Comic sens MC', 8, 'bold'))
label_malos.place(x=400, y= 400, width=50, height=35)

ventana.mainloop()
