# grava numeros impares e pares em arquivos separados

def separaParesImpares():
    with open("impares.txt", "w") as impares, open("pares.txt", "w") as pares:
        for n in range(0, 10000):
            if n % 2 == 0:
                pares.write(f"{n}\n")
            else:
                impares.write(f"{n}\n")


if __name__ == "__main__":
    separaParesImpares()
