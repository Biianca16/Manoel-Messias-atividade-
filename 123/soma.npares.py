#programa que mostra a somatoria dos numeros pares de 1 ate 500 com for
for i in range (1,501):
    if i%2==0:
        somatorio=0
        for j in range(1,i+1):
            somatorio+=j
        print("o somatorio do numero: ",i,"e: ",somatorio)
print("fim do programa")