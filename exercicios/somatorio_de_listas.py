#Este código recebe do usuario o tamanho de uma lista, para somar todos os valores dela.

tamanhoLista=int(input())               #Lendo quantos elementos tera a lista.
lista_Num = list(range(tamanhoLista))   #define o tamanho da lista.

lista_Num = map(int, input().split())   
# Lendo a lista: o input recebe todos os valores dena mesma linha sendo separados por " ".
# ".split" -> para separar a lista em diversos elementos
# "map(int, ...)" -> altera o tipo dos elementos para inteiro, para que a função "sum" funcione

print(sum(list(lista_Num))) # Imprime a soma dos valores da "lista_Num"