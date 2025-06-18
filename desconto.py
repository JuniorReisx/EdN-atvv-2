nomeProduto = "Camiseta"
precoOriginal = 50.00
porcentagemDesconto = 20

# Cálculo
valorDesconto = precoOriginal * (porcentagemDesconto / 100)
precoFinal = precoOriginal - valorDesconto

print(f"Produto: {nomeProduto}")
print(f"Preço Original: R$ {precoOriginal:.2f}")
print(f"Desconto: {porcentagemDesconto}%")
print(f"Valor do Desconto: R$ {valorDesconto:.2f}")
print(f"Preço com Desconto: R$ {precoFinal:.2f}")
