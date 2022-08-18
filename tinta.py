altura = float(input("Informe a altura do cilindro em metros: "))
raio = float(input("Informe a altura do cilindro em metros: "))
PI = 3.14

areaCilindro = 2*PI*raio*(raio + altura)

lataTotalUmaLata = 15
valorLata = 50

quantDeLata = areaCilindro / lataTotalUmaLata
custo = quantDeLata * valorLata

print("Quantidade de latas utilizadas: " + str(quantDeLata))
print("Custo da printura: R$ " + str(custo))
 