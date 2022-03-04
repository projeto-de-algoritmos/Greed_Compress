import heapq
import os

def compactar(self):
	filename, file_extension = os.path.splitext(self.path)
	caminho_saida = filename + ".bin"

	with open(self.path, 'r+') as file, open(caminho_saida, 'wb') as saida:
		texto = file.read()
		texto = texto.rstrip()

		numero_vezes = self.cria_frequencia(texto)
		self.cria_heap(numero_vezes)
		self.mistura_nodes()
		self.cria_codes()

		formata_texto = self.get_texto_formatado(texto)
		formata_texto_comprimido = self.formata_Texto(texto_formatado)

		b = self.recebe_bit(formata_texto_comprimido)
		saida.write(bytes(b))

	print("Compressed")
	return caminho_saida





