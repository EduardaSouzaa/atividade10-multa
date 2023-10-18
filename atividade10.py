# Exercício Python 10: faça um algoritimo que receba a velocidade em Km/h de um veiculo e:
# se maior que 60km/h aplicar multa de 7 vezes a da velocidade permitida
velocidade = float(input("velocidade: "))
if velocidade > 60:
    print(f"por conta da alta velocidade você tomara uma multa de {velocidade*7:.2f}")
else: 
    print("dentro da lei")