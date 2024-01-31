#

def juntaNumeros():
    """
    Junta numeros dos arquivos pares.txt e impares.txt
    """

    with open("impares.txt") as impares, open("pares.txt") as pares, open("pareseimpares.txt", "w") as juntado:
        impares = map(int, impares)
        pares = map(int, pares)
        
        juntos = list(pares) + list(impares)

        for numero in sorted(juntos):
            juntado.write(f"{numero}\n")




if __name__ == "__main__":
    juntaNumeros()

