# Solicita a quantidade de morangos em Kg
quantidade_morangos = float(input("Digite a quantidade de morangos em Kg: "))

# Solicita a quantidade de maçãs em Kg
quantidade_macas = float(input("Digite a quantidade de maçãs em Kg: "))

# Calcula o preço dos morangos
if quantidade_morangos <= 5:
    preco_morangos = quantidade_morangos * 2.50
else:
    preco_morangos = quantidade_morangos * 2.20

# Calcula o preço das maçãs
if quantidade_macas <= 5:
    preco_macas = quantidade_macas * 1.80
else:
    preco_macas = quantidade_macas * 1.50

# Calcula o preço total
preco_total = preco_morangos + preco_macas

# Aplica o desconto, se necessário
if quantidade_morangos + quantidade_macas > 8 or preco_total > 25.00:
    desconto = 0.10 * preco_total
    preco_total -= desconto

print(f"Valor a ser pago pelo cliente: R$ {preco_total:.2f}")