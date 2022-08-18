hora = int(input("Digite as horas (1-24): "))
minuto = int(input("Digite os minutos: "))
segundo = int(input("Digite os segundos: "))

horas1 = hora * (60*60)
minutos1 = minuto * 60

totalHora = horas1 + minutos1 + segundo 
dia = 24 * 3600

horafinal = dia - totalHora

print("O tempo em horas que trascorreram até o momento foi de: " + str(horafinal))