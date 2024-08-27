#Ejercicio 2.1 Calculadora
from tkinter import *

#Cálculos
def Suma():
    num1=int(entry.get()) if entry.get() else 0
    num2=int(entry2.get()) if entry2.get() else 0
    suma= num1 + num2
    entry.delete(0, END)  
    entry.insert(0, str(suma))


#ventana
ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("360x450")
#Color de ventana
ventana.configure(bg="#f5eb9d")
#Ventana que se pueda agrandar 
ventana.resizable(False,True)

#Entry
entry= Entry (ventana,textvariable="0", bg="white", state='readonly')
entry.place(x=200, y= 10, width=130, height=20)
entry.insert(0,"0")

entry2= Entry (ventana,textvariable="0", bg="white", state='readonly')
entry2.place(x=200, y= 60, width=130, height=20)
entry2.insert(0,"0")

entry_res= Entry (ventana,textvariable="0", bg="white", state='readonly')
entry_res.place(x=200, y= 110, width=130, height=20)
entry_res.insert(0,"0")

#Botones
button=Button(ventana,text="+",borderwidth=2, height=4, width=10,anchor="center",bg="#affad7", font= ('Comic sens MC',11,'bold'),command=Suma)
button.pack()
button.place(x=30, y=160)

button_menos=Button(ventana,text="-",borderwidth=2, height=4, width=10,anchor="center",bg="#affad7", font= ('Comic sens MC',11,'bold'),command=Suma)
button_menos.pack()
button_menos.place(x=130, y=160)

button_mult=Button(ventana,text="*",borderwidth=2, height=4, width=10,anchor="center",bg="#affad7", font= ('Comic sens MC',11,'bold'),command=Suma)
button_mult.pack()
button_mult.place(x=30, y=250)

button_div=Button(ventana,text="/",borderwidth=2, height=4, width=10,anchor="center",bg="#affad7", font= ('Comic sens MC',11,'bold'),command=Suma)
button_div.pack()
button_div.place(x=130, y=250)

button_por=Button(ventana,text="%",borderwidth=2, height=4, width=10,anchor="center",bg="#affad7", font= ('Comic sens MC',11,'bold'),command=Suma)
button_por.pack()
button_por.place(x=230, y=250)

button_clear=Button(ventana,text="Clear",borderwidth=2, height=4, width=10,anchor="center",bg="#affad7", font= ('Comic sens MC',11,'bold'),command=Suma)
button_clear.pack()
button_clear.place(x=230, y=160)

#Labels
label=Label(ventana,text="Primer número",bg="#fcf8d4",fg="#785330", font= ('Calibri',12))
label.place(x=20, y= 10, width=120, height=20)

label2=Label(ventana,text="Segundo número",bg="#fcf8d4",fg="#785330", font= ('Calibri',12))
label2.place(x=20, y= 60, width=140, height=20)

label_res=Label(ventana,text="Resultado",bg="#fcf8d4",fg="#785330", font= ('Calibri',12))
label_res.place(x=20, y= 110, width=100, height=20)

ventana.mainloop()