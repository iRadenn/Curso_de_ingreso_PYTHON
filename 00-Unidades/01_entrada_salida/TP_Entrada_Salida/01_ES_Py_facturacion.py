import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Ignacio
apellido: Orellana
---
TP: ES_Facturaciones
---
Enunciado:
Para el departamento de facturación:
    A.	Ingresar tres precios de productos y mostrar la suma de los mismos.
    B.	Ingresar tres precios de productos y mostrar el promedio de los mismos.
	C.	ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%).
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Producto 1")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_importe_1 = customtkinter.CTkEntry(master=self)
        self.txt_importe_1.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Producto 2")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_importe_2 = customtkinter.CTkEntry(master=self)
        self.txt_importe_2.grid(row=1, column=1)

        self.label_3 = customtkinter.CTkLabel(master=self, text="Producto 3")
        self.label_3.grid(row=2, column=0, padx=20, pady=10)
        
        self.txt_importe_3 = customtkinter.CTkEntry(master=self)
        self.txt_importe_3.grid(row=2, column=1)
        
        self.btn_total = customtkinter.CTkButton(master=self, text="TOTAL", command=self.btn_total_on_click)
        self.btn_total.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_promedio = customtkinter.CTkButton(master=self, text="PROMEDIO", command=self.btn_promedio_on_click)
        self.btn_promedio.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_total_iva = customtkinter.CTkButton(master=self, text="TOTAL c/IVA", command=self.btn_total_iva_on_click)
        self.btn_total_iva.grid(row=5, pady=10, columnspan=2, sticky="nsew")

    def btn_total_on_click(self):
        producto1 = float(self.txt_importe_1.get())
        producto2 = float(self.txt_importe_2.get())
        producto3 = float(self.txt_importe_3.get())

        total = producto1 + producto2 + producto3

        alert("Resultado", "La suma entre {0}, {1}, {2} nos da un total de: {3}".format(producto1, producto2, producto3, total))
        pass

    def btn_promedio_on_click(self):
        producto1 = float(self.txt_importe_1.get())
        producto2 = float(self.txt_importe_2.get())
        producto3 = float(self.txt_importe_3.get())

        total = producto1 + producto2 + producto3

        promedio = total/3

        alert("Resultado", "El promedio entre {0}, {1}, {2} nos da un total de: {3}".format(producto1, producto2, producto3, promedio))
        pass

    def btn_total_iva_on_click(self):
        producto1 = float(self.txt_importe_1.get())
        producto2 = float(self.txt_importe_2.get())
        producto3 = float(self.txt_importe_3.get())

        total = producto1 + producto2 + producto3

        iva = ((21/100)*total)

        total_final = total + iva

        alert("Resultado", "La suma entre {0}, {1}, {2} nos da un total de: {3}, mas el 21% de IVA ({4}), nos daria: {5}".format(producto1, producto2, producto3, total, iva, total_final))
        pass      
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()