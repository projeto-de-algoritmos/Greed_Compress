from huffman import HuffmanCoding
import tkinter as tk
from tkinter import *
from tkinter import filedialog

import customtkinter


def buscarArquivos():
    nomedoarquivo = filedialog.askopenfilename(initialdir="/",
                                          title="Selecione um arquivo",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("all files",
                                                      "*.*")))
    buscarArquivos.caminho = str(nomedoarquivo)



    pathh.insert(tk.END, nomedoarquivo)

# Comprimir
def compress():

    local = buscarArquivos.caminho

    h = HuffmanCoding(local)
    compress.output_path = h.compress()

    prnt = ("Local de descompressão: " + compress.output_path + "\n\n")

    text.insert(tk.END, prnt)

# Descomprimir
def decompress():
    local = buscarArquivos.caminho

    h = HuffmanCoding(local)

    decom_path = h.decompress(h.compress())
    prnt = ("Local de descompressão: " + decom_path + "\n\n")

    text.insert(tk.END, prnt)

# Limpar caixa de texto
def limpar():
    text.delete('1.0', END)

new_c = "forestgreen"


#----Nome da Janela-----#
root = customtkinter.CTk()
root.title("Compressor de Texto")


# ---Wirgets da aplicação---#
mainframe = customtkinter.CTkFrame(root)
mainframe.grid(column=0, row=0, sticky=(N, S, E, W))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)




#----Menu----#
root.option_add('*tearOff', FALSE)

menubar = Menu(root)
root.config(menu=menubar)

menu_file = Menu(menubar)
menu_edit = Menu(menubar)
menubar.add_cascade(menu=menu_file, label='Arquivo')
menubar.add_cascade(menu=menu_edit, label='Editar')

menu_file.add_command(label='Novo')

menu_file.add_command(label='Fechar', command=root.destroy)

menu_edit.add_command(label='Copiar')
menu_edit.add_command(label='Colar')


#--Selecionar o arquivo---#
select_file_label = customtkinter.CTkLabel(mainframe,
                                            text="Local do arquivo selecionado:",
                                            width=200,
                                            height=50,
                                            fg_color=None)
select_file_label.grid(row=0, column=0, pady=10, padx=30, sticky=(W))

pathh = customtkinter.CTkEntry(mainframe, width=240)
pathh.grid(row=0, column=1, columnspan=2, pady=5, padx=10, sticky=())

select_file_btn1 = customtkinter.CTkButton(mainframe,
                                            text="Selecione um Arquivo",
                                           command=buscarArquivos,
                                            fg_color=None,
                                            border_width=2,
                                            border_color=new_c,
                                            hover_color=new_c)
select_file_btn1.grid(row=0, column=3, pady=5, padx=10)



#--Selecionar a ação de Comprimir e descomprimir--#
select_audit_label = customtkinter.CTkLabel(mainframe,
                                            text="Selecione uma ação:",
                                            height=50,
                                            width=200,
                                            fg_color=None)
select_audit_label.grid(row=1, column=0, pady=10, padx=30, sticky=(W))



#--Opções--#
mob_btn = customtkinter.CTkButton(mainframe,
                                  text="Comprimir",
                                  command=compress,
                                  fg_color=None,
                                  border_width=2,
                                  border_color=new_c,
                                  hover_color=new_c)
mob_btn.grid(row=1, column=1, pady=5, padx=10, sticky=())

cont_btn = customtkinter.CTkButton(mainframe,
                                    text="Descomprimir",
                                   command=decompress,
                                    fg_color=None,
                                    border_width=2,
                                    border_color=new_c,
                                    hover_color=new_c)
cont_btn.grid(row=1, column=2, pady=5, padx=10)


#-- Botões ---#

text = tk.Text(mainframe, wrap=WORD, height=30, width=100)
text.grid(row=2, column=0, columnspan=5, padx=35, pady=20)

clear_btn = customtkinter.CTkButton(mainframe,
                                    text="Limpar",
                                    command=limpar,
                                    fg_color=None,
                                    border_width=2,
                                    border_color=new_c,
                                    hover_color=new_c)
clear_btn.grid(row=4, column=4, pady=20, padx=10)




root.mainloop()
