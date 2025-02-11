#Teste de como funciona a funcao "sorted()"

tamanhoLista = int(input())                 #Recebe o tamanho da lista

lista_Num = list(range(tamanhoLista))       #Declara uma lista com o tamanho escolhido

lista_Num = map(int, input().split())       
#Lê a lista de numeros numa linha unica separada por espaco
# ".split" -> para separar a lista em diversos elementos
# "map(int, ...)" -> altera o tipo dos elementos para inteiro, para que a função "sorted()" funcione

print(sorted(list(lista_Num)))          # Imprime a lista_Num de forma ordenada