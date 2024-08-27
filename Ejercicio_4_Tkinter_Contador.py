#Ejercicio 1.4 – Contador.
from tkinter import *

#Cálculos
def Calcular_contador():
    cont=int(entry.get()) if entry.get() else 0
    cont+=1
    entry.config(state='normal')
    entry.delete(0, END)  
    entry.insert(0, str(cont))
    entry.config(state='readonly')
    
def Calcular_contador_decreciente():
    cont=int(entry.get()) if entry.get() else 0
    cont-=1
    entry.config(state='normal')
    entry.delete(0, END)  
    entry.insert(0, str(cont))
    entry.config(state='readonly')
    
def Calcular_reset():
    cont=int(entry.get()) if entry.get() else 0
    cont =0
    entry.config(state='normal')
    entry.delete(0, END)  
    entry.insert(0, str(cont))
    entry.config(state='readonly')

#ventana
ventana = Tk()
ventana.title("Contador")
ventana.geometry("680x300")
#Color de ventana
ventana.configure(bg="#f5eb9d")
#Ventana que se pueda agrandar 
ventana.resizable(True,True)

#marco
marco= LabelFrame(ventana, text="Contador", bg="#fcf8d4", font= ('Times New Roman',12,'italic','bold'))
marco.place(x=90, y= 60, width=500, height=200)

#Entry
entry= Entry (ventana,textvariable="0", bg="white", state='readonly')
entry.place(x=200, y= 150, width=130, height=20)
entry.config(state='normal')
entry.insert(0,"0")
entry.config(state='readonly')

#Botones
button=Button(ventana,text="Count Up",borderwidth=2, height=1, width=7,anchor="center",bg="#affad7", font= ('Comic sens MC',8,'bold'),command=Calcular_contador)
button.pack()
button.place(x=350, y=147)

button_down=Button(ventana,text="Count Down",borderwidth=2, height=1, width=9,anchor="center",bg="#affad7", font= ('Comic sens MC',8,'bold'),command=Calcular_contador_decreciente)
button_down.pack()
button_down.place(x=427, y=147)

button_reset=Button(ventana,text="Reset",borderwidth=2, height=1, width=7,anchor="center",bg="#5ff5af", font= ('Comic sens MC',8,'bold'),command=Calcular_reset)
button_reset.pack()
button_reset.place(x=520, y=147)


#Label
label=Label(ventana,text="Contador",bg="#fcf8d4",fg="#785330", font= ('Impact',17))
label.place(x=98, y= 133, width=100, height=50)

ventana.mainloop()
