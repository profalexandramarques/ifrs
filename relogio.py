#Relógio na tela
import tkinter as tk, time

tela = tk.Tk(); 
tela.geometry("250x150")
tela.title("Relógio")
hora = tk.Label(tela, font=("Arial", 40)); 
hora.pack()

#Função recursiva
def visor():
    hora.config(text=time.strftime("%H:%M:%S"))
    tela.after(1000, visor)

#Programa Principal
visor(); 
tela.mainloop()