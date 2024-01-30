#

def juntaNumeros():
    """
    Junta numeros dos arquivos pares.txt e impares.txt
    """

    numeros_pares = numeros_impares = []

    with open("impares.txt") as impares,  open("pares.txt") as pares:
        numeros_pares = pares.readlines()
        numeros_impares = impares.readlines()

    with open("pareseimpares.txt", "w") as juntado:

        #max = len(numeros_pares) if len(numeros_pares) > len(numeros_impares) else len(numeros_impares)
        
        par = int(numeros_pares.pop(0))
        impar = int(numeros_impares.pop(0))

        while len(numeros_pares) > 0 and len(numeros_impares) > 0:
            
            #print(par, impar)

            while par > impar and len(numeros_impares) > 0:
                juntado.write(f"{impar}\n")
                impar = int(numeros_impares.pop(0))

            while impar > par and len(numeros_pares) > 0:
                juntado.write(f"{par}\n")
                par = int(numeros_pares.pop(0))

        if par > impar:
            juntado.write(f"{impar}\n")
            juntado.write(f"{par}\n")
        else:
            juntado.write(f"{par}\n")
            juntado.write(f"{impar}\n")

        if len(numeros_pares) > 0:
            juntado.writelines(numeros_pares)
        elif len(numeros_impares) > 0:
            juntado.writelines(numeros_impares)



if __name__ == "__main__":
    juntaNumeros()

