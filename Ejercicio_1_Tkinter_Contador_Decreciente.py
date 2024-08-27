#Ejercicio 1.2 - Contador Decreciente.
from tkinter import *

#Cálculos
def Contador_decrecer():
    cont=int(entry.get()) if entry.get() else 88
    cont-=1
    entry.config(state='normal')
    entry.delete(0, END)  
    entry.insert(0, str(cont))
    entry.config(state='readonly')
    
#ventana
ventana = Tk()
ventana.title("ContDecreciente")
ventana.geometry("580x300")

#Tamaño mínimo y máximo de ventana
ventana.minsize(300,200)
ventana.maxsize(1300,800)

#Color de ventana
ventana.configure(bg="#c2987e")

#Ventana que se pueda agrandar 
ventana.resizable(True,True)

#marco
marco= LabelFrame(ventana, text="Contador Decreciente", bg="#ebd2be", font= ('Times New Roman',12,'italic','bold'))
marco.place(x=90, y= 60, width=400, height=200)

#Botones
button=Button(ventana,text="-",borderwidth=2, height=1, width=7,anchor="center",bg="#d97971", font= ('Comic sens MC',8,'bold'),command=Contador_decrecer)
button.pack()
button.place(x=350, y=147)

#Label
label=Label(ventana,text="Contador",bg="#ebd2be",fg="#912424", font= ('Times New Roman',13, "bold"))
label.place(x=128, y= 133, width=100, height=50)

#Entry
entry= Entry (ventana,textvariable="88", bg="white", state='readonly')
entry.place(x=220, y= 150, width=115, height=20)
entry.config(state='normal')
entry.insert(0, "88")
entry.config(state='readonly')

ventana.mainloop()