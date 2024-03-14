#programa que calcula o fatorial de um numero que o usuario digita usando while=true
while True:
    n=int(input("digite um numero inteiro: "))
    fatorial=1
    for i in range(1, n+1):
        fatorial = fatorial * i
    print(fatorial)
    continuar = input("deseja continuar? (s/n)")
    if continuar == "n":
        break