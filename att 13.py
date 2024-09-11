# Crie um programa que receba um número do usuário e informe se ele é positivo, negativo ou zero.

numero = float(input("Digite u, número: "))

if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("Zero")