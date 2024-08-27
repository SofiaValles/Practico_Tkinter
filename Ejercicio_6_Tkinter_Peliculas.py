#Ejercicio 2.2 Películas.
from tkinter import *

def Agregar():
    peli = entry.get().strip()
    if peli:
        lista.insert(END, peli)
        entry.delete(0, END)

#ventana
ventana = Tk()
ventana.title("Películas")
ventana.geometry("600x400")
ventana.configure(bg="#c688d1")
ventana.resizable(False, False)

#Botón
button=Button(ventana,text="Añadir",borderwidth=2, height=1, width=7,anchor="center",bg="#DAA38F", font= ('Comic sens MC',8,'bold'), command=Agregar)
button.place(x=93, y=147)

#Entrada
entry = Entry(ventana, bg="#ccc3fa")
entry.place(x=30, y=110, width=200, height=20)

#Lista películas
lista=Listbox(ventana, bg="#E8D4BB")
lista.place(x=280, y=50, width=280, height=320)

#Etiquetas
label_entr= Label(ventana,text="Escribe el título de tu película!",bg="#c688d1", fg="#181042", font=('Times New Roman', 12, 'bold'))
label_entr.place(x=27, y=80, width=210, height=20)

label_list= Label(ventana, text="¡Películas!",bg="#c688d1", fg="#4b1854", font=('Impact', 24))
label_list.place(x=350, y=15, width=140, height=35)

ventana.mainloop()
