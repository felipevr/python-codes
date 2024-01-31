# le o entrada.txt e imprime conforme as regras

LARGURA = 79

with open("entrada.txt") as entrada:
   for linha in entrada.readlines():
       char1 = linha[0]
       if char1 == ';':
           continue # ignorar
       elif char1 == '>':
           print(linha[1:].rjust(LARGURA))
       elif char1 == '*':
           print(linha[1:].center(LARGURA))
       elif char1 == '<':
           print(linha[1:])
       else:
           print(linha)
           
   pass 

