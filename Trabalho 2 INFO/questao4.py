a = float(input("Digite o primeiro valor: "))                 
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))

# Usar propriedade distributiva para ordenar os valores
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b

# Apresentar os valores em ordem crescente
print("Os valores em ordem crescente são:", a, b, c)