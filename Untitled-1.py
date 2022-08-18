precoProduto = float(input("Digite o preço do produto: "))

avista = (precoProduto*5/100) - precoProduto

duasVsJuros = precoProduto / 2

tresVsCJuros = (precoProduto + 5/100) / 3

print("Preço do produto à vista:" + str(avista))

print("Preço do produto em 2 vezes sem juros:" + str(duasVsJuros))

print("Preço do produto em 3 vezes com 5% de juros:" + str(tresVsCJuros))