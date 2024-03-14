#programa que calcula o valor de um numero que o usuario
resp="sim"
while resp=="sim":
    n=int(input("digite um numero: "))
    fatorial=1
    for i in range(1,n+1):
        fatorial=fatorial*i
    print("o fatorial de",n,"e",fatorial)
    resp=input("deseja calcular o fatorial de outro numero? (sim/nao)")    