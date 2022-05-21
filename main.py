vel = float(input("Digite a velocidade do seu carro em Km/h: "))

if vel>80:
    mult=vel-80
    mult=mult*5
    print(" O valor da multa é de: %.2f RS "%mult)
else:
    print("Velocidade dentro do limite")