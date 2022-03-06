import heapq
import os

class HuffmanCoding:
    def __init__(self, path):
        self.path = path
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    class HeapNode:
        def __init__(self, char, freq):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None

        # definir comparadores
        def __lt__(self, outro):
            return self.freq < outro.freq

        def __eq__(self, outro):
            if (outro == None):
                return False
            if (not isinstance(outro, HeapNode)):
                return False
            return self.freq == outro.freq

    # funções para comprensão:

    def cria_frequencia(self, texto):
        frequencia = {}
        for caracter in texto:
            if not caracter in frequencia:
                frequencia[caracter] = 0
            frequencia[caracter] += 1
        return frequencia

    def make_heap(self, frequencia):
        for chave in frequencia:
            node = self.HeapNode(chave, frequencia[chave])
            heapq.heappush(self.heap, node)

    def merge_nodes(self):
        while (len(self.heap) > 1):
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = self.HeapNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.heap, merged)

    def make_codes_helper(self, root, no_atual):
        if (root == None):
            return

        if (root.char != None):
            self.codes[root.char] = no_atual
            self.reverse_mapping[no_atual] = root.char
            return

        self.make_codes_helper(root.left, no_atual + "0")
        self.make_codes_helper(root.right, no_atual + "1")

    def make_codes(self):
        root = heapq.heappop(self.heap)
        codigo_atual = ""
        self.make_codes_helper(root, codigo_atual)

    def codificado(self, texto):
        encoded_text = ""
        for caracter in texto:
            encoded_text += self.codes[caracter]
        return encoded_text

    def bloco_codificado(self, encoded_text):
        extra_padding = 8 - len(encoded_text) % 8
        for i in range(extra_padding):
            encoded_text += "0"

        padded_info = "{0:08b}".format(extra_padding)
        encoded_text = padded_info + encoded_text
        return encoded_text
