""" Importando tkinter """
from tkinter import *
from tkinter import ttk

#Cores

cor1 = "#2596be"  # azul
cor2 = "#000000"  # marrom escuro
cor3 = "#1a855a"  # verde
cor4 = "#f5fbfb"  # branco
cor5 = "#b11f38" # vermelho

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg = cor1)

# Criando frames
frame_tela = Frame(janela, width = 235, height = 50, bg = cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width = 235, height = 268)
frame_corpo.grid(row=1, column=0)

# Criando Botões

b1 = Button(frame_corpo, text = "C", width = 11, height = 2, bg = cor4, font = "Ivy 13 bold", relief = RAISED, overrelief=RIDGE)
b1.place(x=0, y=0)

b2 = Button(frame_corpo, text = "%", width = 5, height = 2, bg = cor4,font = "Ivy 13 bold", relief = RAISED, overrelief=RIDGE)
b2.place(x=118, y=0)

b3 = Button(frame_corpo, text = "/", width = 5, height = 2, bg = cor5, font = "Ivy 13 bold", relief = RAISED, overrelief=RIDGE)
b3.place(x=177, y=0)

janela.mainloop()



