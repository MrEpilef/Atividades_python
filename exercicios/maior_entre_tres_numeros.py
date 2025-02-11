#Recebe 3 valores em linhas diferentes, e retorna o de maior valor entre os tres
a=int(input('Insira o primeiro valor: '))
b=int(input('Insira o segundo valor: '))
c=int(input('Insira o terceiro valor: '))

#tratamento simplificado de dados / nao aconcelhado o uso, pois nao valida possibilidade de absurdo e/ou tipo de dado. 
if a>=b and a>=c:
    print(a)
if b>a and b>c:
    print(b)
if c>a and c>b:
    print(c)
