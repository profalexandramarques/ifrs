#Bandeira da França usando Frames
import tkinter as tk

#Criar a tela
tela = tk.Tk()
#Define o título da tela
tela.title("Bandeira França")
#Define o tamanho da tela
tela.geometry("240x200")
tela.frame1 = tk.Frame(bg="blue", height=200, width=80)
tela.frame2 = tk.Frame(bg='white', height=200, width=80)
tela.frame3 = tk.Frame(bg='red', height=200, width=80)
tela.frame1.pack(side="left")
tela.frame2.pack(side="left")
tela.frame3.pack(side="left")
tk.mainloop()  