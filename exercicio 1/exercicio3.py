#programa que imprime cinco vezes um numero lido multiplicado por 3
resp="sim"
while resp=='sim':
    num=int(input("digite umnumero: "))
    r=num*3
    print(r)
    resp=input("deseja continuar")
    if resp!="sim":
       break
print("fim do programa")