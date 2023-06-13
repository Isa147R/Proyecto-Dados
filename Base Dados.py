import random

def lanzar_dados(num_dados, num_lados):
    resultados = []
    for _ in range(num_dados):
        resultado = random.randint(1, num_lados)
        resultados.append(resultado)
    return resultados

def main():
    num_dados = int(input("Ingrese el número de dados: "))
    num_lados = int(input("Ingrese el número de lados: "))

    resultados = lanzar_dados(num_dados, num_lados)
    print("Resultados de los lanzamientos:")
    for i, resultado in enumerate(resultados, start=1):
        print(f"Dado {i}: {resultado}")

if __name__ == '__main__':
    main()
