#Ejercicio 2.2 Películas.
from tkinter import *

def Agregar():
    peli = entry_var.get()
    caracteres = list(peli)

    if "  " in peli or caracteres[0] == " ":
        entry_var.set("")
        modal_espacios = Toplevel(ventana)
        modal_espacios.title("Error")
        modal_espacios.geometry("300x150")
        modal_espacios.configure(bg="#f5eb9d")

        label_error= Label(modal_espacios, text="No puede ingresar tantos espacios!",bg="#f5eb9d", fg="#4b1854", font=('Comic sens MC', 12))
        label_error.place(x=25 , y=25, width=250, height=35)

        boton_cerrar_espacios= Button(modal_espacios,text="Aceptar",borderwidth=2, height=1, width=8,anchor="center",bg="#DAA38F", font= ('Comic sens MC',8,'bold'), command=modal_espacios.destroy)
        boton_cerrar_espacios.place(x=110, y=80)
        
        

        if peli in lista.get(0, END):
            modal = Toplevel(ventana)
            modal.title("Error")
            modal.geometry("300x150")
            modal.configure(bg="#f5eb9d")
            
            label_error2= Label(modal, text="Su película ya ha sido cargada",bg="#f5eb9d", fg="#593822", font=('Times New Roman', 12))
            label_error2.place(x=40, y=25, width=220, height=35)

            boton_cerrar= Button(modal,text="Aceptar",borderwidth=2, height=1, width=8,anchor="center",bg="#DAA38F", font= ('Comic sens MC',8,'bold'), command=modal.destroy)
            boton_cerrar.place(x=110, y=80)
            entry_var.set("")
    else:
        lista.insert(END, peli)
        entry_var.set("")
        

    

#ventana
ventana = Tk()
ventana.title("Películas")
ventana.geometry("600x400")
ventana.configure(bg="#c688d1")
ventana.resizable(False, False)

#Botón
button=Button(ventana,text="Añadir",borderwidth=2, height=1, width=8,anchor="center",bg="#DAA38F", font= ('Comic sens MC',8,'bold'), command=Agregar)
button.place(x=93, y=147)

#Entrada
entry_var = StringVar(value="")
entry = Entry(ventana, bg="#ccc3fa",textvariable=entry_var)
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