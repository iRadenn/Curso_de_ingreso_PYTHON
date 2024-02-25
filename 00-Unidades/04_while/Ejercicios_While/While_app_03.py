import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Ignacio
apellido: Orellana
---
Ejercicio: while_03
---
Enunciado:
Al presionar el botón ‘Pedir clave’, solicitar al usuario que ingrese una contraseña mediante prompt. 
Comprobar que la contraseña ingresada sea ‘utn750’. En caso de no coincidir, volver a solicitarla hasta que coincidan.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_pedir_clave = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_pedir_clave_on_click)
        self.btn_pedir_clave.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_pedir_clave_on_click(self):

        #Prompt se utiliza para poder ingresar datos mediante una ventana de texto
        clave = prompt("", "Ingrese la clave")
        clave = str(clave)
        #El simbolo "!=" se utiliza para devolver TRUE si es q ambos operandos no son iguales, en este caso al no ser igual la clave, vuelve a solicitar la misma
        while clave != "utn750":
            clave = prompt("", "Ingrese la clave nuevamente")
            clave = str(clave)
        
        alert("", "La clave se ingreso correctamente")
        pass
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()