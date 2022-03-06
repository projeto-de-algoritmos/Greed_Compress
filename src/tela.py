from huffman import HuffmanCoding
from tkinter import ttk
from tkinter import *
from tkinter import filedialog


def buscarArquivos():
    nomedoarquivo = filedialog.askopenfilename(initialdir="/",
                                          title="Selecione um arquivo",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("all files",
                                                      "*.*")))
    buscarArquivos.caminho = str(nomedoarquivo)

    label_file_explorer.configure(text="Local do Arquivo: " + nomedoarquivo)

def compress():

    local = buscarArquivos.caminho

    h = HuffmanCoding(local)
    compress.output_path = h.compress()
    print("Local de compressão: " + compress.output_path)

def decompress():
    local = buscarArquivos.caminho

    h = HuffmanCoding(local)

    decom_path = h.decompress(h.compress())
    print("Local de descompressão: " + decom_path)

#Cria a Janela
window = Tk()

# Título da Janela
window.title('Comprimir arquivo')

# Tamanho da tela
window.geometry("600x200")

# Cor do fundo
window.config(background="white")

# Selecionar arquivo
label_file_explorer = Label(window,
                            text="Local do arquivo",
                            width=90, height=3,
                            fg="blue")

button_explore = Button(window,
                        text="Selecione um Arquivo",
                        command=buscarArquivos)
# Tela design
compress_button = ttk.Button(window,
    text="Comprimir",
    command=compress
)

decompress_button = ttk.Button(window,
    text="Descomprimir",
    command=decompress
)

button_exit = Button(window,
                     text="Sair",
                     command=exit)


label_file_explorer.grid(column=1, row=1)

button_explore.grid(column=1, row=2)

compress_button.grid(column=1, row=3)

decompress_button.grid(column=1, row=4)

button_exit.grid(column=1, row=5)

window.mainloop()

