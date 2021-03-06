#https://www.hackerrank.com/challenges/tree-huffman-decoding/problem#:~:text=Huffman%20coding%20assigns%20variable%20length,character%20contain%20a%20code%20digit.

#Complete the function decode_huff in the editor below. It must return the decoded string.

#decode_huff has the following parameters:

#root: a reference to the root node of the Huffman tree
#s: a Huffman encoded string


def decodeHuff(root, s):
    atual = root

    resultado = ''

    vazio = None
    
    for code in s:
        if int(code) == 0:
            atual = atual.left
        else:
            atual = atual.right
        if atual.left == vazio and atual.right == vazio:

            resultado += atual.data
            atual = root

    print(resultado)