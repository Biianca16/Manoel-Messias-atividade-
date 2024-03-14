#tabuada de multiplicacao de um numero qualquer com while
while True:
    n = int(input("digite um numero pra ver a tabuada: "))
    print("tabuada de multiplicacao de numero", n)
    i = 1
    while i <= 10:
        print(n, "x", i, "=", n*i)
        i +=1
    continua=input("deseja continuar? (sim/nao)")
    if continua=="nao":
       break