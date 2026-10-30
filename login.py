#Tela de Login
import tkinter as tk
from tkinter import messagebox

# Criação da janela principal
tela = tk.Tk()
tela.title("Login")
tela.geometry("350x150")
#Não redimensinar a tela
tela.resizable(False, False) 

#Criar o usuário 
lblusuario = tk.Label(text="Usuário")
lblusuario.pack()
cxusuario = tk.Entry(tela)
cxusuario.pack()

#Cria a senha
labelsenha = tk.Label(text="Senha")
labelsenha.pack()
cxsenha = tk.Entry(tela,show="*")
cxsenha.pack()

#Cria um frame para os botões
frame_botoes = tk.Frame(tela)
frame_botoes.pack(side="bottom",pady=20)

#Função do botão Login
def logar():
    usuario = cxusuario.get()
    if usuario.strip() == "":
       messagebox.showwarning("Aviso", "Digite o usuário!") 

    senha = cxsenha.get()
    if senha == "12345":
        messagebox.showinfo("Mensagem", 
                            "Login realizado com sucesso!")  
        tela.destroy()          
    else:
        messagebox.showerror("Erro", "Senha incorreta!")

btnlogin = tk.Button(frame_botoes, text="Login",width=15,
                     command=logar)
btnlogin.pack(side="left",padx=5)

#Função do botão Sair
def sair():
    resposta = messagebox.askyesno("Sair", 
                 "Você tem certeza que deseja fechar o programa?")
    if resposta == True:
        # Fecha a tela principal
        tela.destroy() 
    else:
        messagebox.showinfo("Continuar", "Continuar!")

#Criar um botão para Sair
botaosair = tk.Button(frame_botoes, 
                      text="Cancelar",
                      width=15,command=sair)
botaosair.pack(side="left",padx=5)

tela.mainloop()

