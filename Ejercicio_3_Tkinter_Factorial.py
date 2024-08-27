#Ejercicio 1.3 – Factorial.
from tkinter import *

def Calcular_factorial():
    numero = int(entry.get()) if entry.get() else 0
    factorial = 1

    # Calcular factorial
    for i in range(1, numero + 1):
        factorial *= i

    entry_factorial.config(state='normal')
    entry_factorial.delete(0, END)
    entry_factorial.insert(0, str(factorial))
    entry_factorial.config(state='readonly')

    numero += 1
    entry.config(state='normal')
    entry.delete(0, END)
    entry.insert(0, str(numero))
    entry.config(state='readonly')
    

#ventana
ventana = Tk()
ventana.title("Contador")
ventana.geometry("680x300")
#Color de ventana
ventana.configure(bg="#FED8A6")
#Ventana que se pueda agrandar 
ventana.resizable(True,True)

#marco
marco= LabelFrame(ventana, text="Factorial", bg="#92ADA4", font= ('Times New Roman',12,'italic','bold'))
marco.place(x=90, y= 60, width=500, height=200)

#Entry
entry= Entry (ventana, bg="white")
entry.place(x=120, y= 150, width=70, height=20)
entry.config(state='normal')
entry.insert(0,"1")
entry.config(state='readonly')

entry_factorial= Entry (ventana, bg="white", state='readonly')
entry_factorial.place(x=320, y= 150, width=170, height=20)
entry_factorial.config(state='normal')
entry_factorial.insert(0,"")
entry_factorial.config(state='readonly')

#Botones
button=Button(ventana,text="Siguiente",borderwidth=2, height=1, width=7,anchor="center",bg="#DAA38F", font= ('Comic sens MC',8,'bold'), command=Calcular_factorial)
button.pack()
button.place(x=500, y=147)

#Label
label_n=Label(ventana,text="n",bg="#92ADA4",fg="#785330", font= ('Impact',16))
label_n.place(x=100, y= 133, width=10, height=50)

label=Label(ventana,text="Factorial (n)",bg="#92ADA4",fg="#785330", font= ('Impact',15))
label.place(x=210, y= 134, width=100, height=50)

ventana.mainloop()
