nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso em Kg: "))
altura = float(input("Digite sua altura: "))

resultado = peso / (altura ** 2)

print(f"Olá {nome}, seu indice de massa corporal é {resultado:.1f}")
