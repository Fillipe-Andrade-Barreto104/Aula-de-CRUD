import tkinter as Tk
from tkinter import ttk

lista_tipos = ["Galão", "Caixa", "Saco", "Unidade"] 

def command():
    nome_material = entry_descriçao.get()
    tipo_unidade = label_tipo_unidade.get()
    quantidade = quantidade_entry.get()

    with open('dados.txt','w') as arquivo:
        arquivo.write("Nome do Material: "+nome_material+"\n")
        arquivo.write("Tipo do Material: "+tipo_unidade+"\n")
        arquivo.write("Quantidade: "+quantidade+"\n")
       


janela = Tk.Tk()

janela.title("Ferramenta de Cadastro de Materiais")

label_descriçao = Tk.Label(text="Descrição do Material")
label_descriçao.grid(row=1, column = 0, padx= 10, pady=10, sticky= 'nswe', columnspan = 4)

entry_descriçao = Tk.Entry()
entry_descriçao.grid(row=2, column =0, padx= 10, pady = 10, sticky= 'nswe', columnspan = 4)

label_tipo_unidade =Tk.Label(text="Tipo da Unidade Do Material")
label_tipo_unidade.grid(row=3, column=0,padx= 10, pady= 10, sticky = 'nswe', columnspan = 2)

label_tipo_unidade = ttk.Combobox(values=lista_tipos)
label_tipo_unidade.grid(row=3, column=2,padx= 10, pady= 10, sticky = 'nswe', columnspan = 2)

label_quantidade = Tk.Label(text="Quantidade: ")
label_quantidade.grid(row=4, column=0,padx= 10, pady= 10, sticky = 'nswe', columnspan = 2)

quantidade_entry = Tk.Entry()
quantidade_entry.grid(row=4, column=2,padx= 10, pady= 10, sticky = 'nswe', columnspan = 2)

botao = Tk.Button(text="Registrar", command = command)
botao.grid(row=5, column=0,padx= 10, pady= 10, sticky = 'nswe', columnspan = 4)

janela.mainloop()

