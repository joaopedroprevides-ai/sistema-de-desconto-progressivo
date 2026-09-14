# Solicita o valor total da compra
valor_compra = float(input("Digite o valor total da compra: R$ "))

# Verifica a porcentagem de desconto
if valor_compra < 200:
    percentual = 5

elif valor_compra < 300:
    percentual = 10

else:
    percentual = 15

# Calcula o desconto
valor_desconto = valor_compra * percentual / 100

# Calcula o valor final
valor_final = valor_compra - valor_desconto

# Exibe os resultados
print(f"\nDesconto aplicado: {percentual}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor total a pagar: R$ {valor_final:.2f}")