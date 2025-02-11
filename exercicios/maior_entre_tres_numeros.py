#Recebe 3 valores em linhas diferentes, e retorna o de maior valor entre os tres
a=int(input('Insira o primeiro valor: '))
b=int(input('Insira o segundo valor: '))
c=int(input('Insira o terceiro valor: '))

if a>=b and a>=c:
    print(a)
if b>a and b>c:
    print(b)
if c>a and c>b:
    print(c)
