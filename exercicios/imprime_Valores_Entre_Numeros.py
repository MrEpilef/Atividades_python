def imprimir_numeros_entre(a, b):
    #Garantir que "a" seja maior ou igual a "b"
    if a>b:
        a, b = b, a #inverte os valores entre a e b

    for numeros in range (a, b+1):
        print(numeros, end=' ') #'end=" "' com intuito de exibir a resposta em uma linha unica

a = int(input())
b = int(input())

imprimir_numeros_entre(a, b)


