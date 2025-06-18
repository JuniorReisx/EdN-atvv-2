valorReais = 100.00
taxaDolar = 5.20
taxaEuro = 6.15

# Cálculo
valor_dolar = valorReais / taxaDolar
taxaEuro = valorReais / taxaEuro

print(f"Valor em Reais: R$ {valorReais:.2f}")
print(f"Em Dólares: US$ {valor_dolar:.2f}")
print(f"Em Euros: € {taxaEuro:.2f}")
