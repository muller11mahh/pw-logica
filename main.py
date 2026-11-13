print("=== CALCULADORA DE DESCONTO ===")
produto = input("Nome do produto: ")
preco = float(input("Preço: R$ "))
desconto = float(input("Desconto (%): "))

valor_desconto =  preço * (desconto / 100)
preco_final = preco - valor_desconto

print(f"\nProduto: {produto}")
print(f"Preço Original: R$ {preco:.2f}")
print(f"Desconto: R$ {valor_desconto:.2f}") 
print(f"Preço final: R$ {preco_final:.2f}")