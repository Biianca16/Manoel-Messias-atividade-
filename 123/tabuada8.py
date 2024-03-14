#tabuada de multiplicacao de um numero qualquer com for
while True:
    n = int(input("digite um numero pra ver a tabuada: "))
    print("tabuada de multiplicacao de numero", n)
    for i in range(1,11):
        print(i, "x", n, "=", i*n)
    continua=input("deseja continuar? (sim/nao)")
    if continua=="nao":
       break