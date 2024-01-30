# Grava multiplos de 4 no arquivo

def multiplos4():
    with open("multiplos4.txt", "w") as multiplos:
        with open("pares.txt") as pares:
            for linha in pares.readlines():
                if int(linha) % 4 == 0:
                    multiplos.write(linha)


if __name__ == "__main__":
    multiplos4()
