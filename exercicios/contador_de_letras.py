#Este algoritmo conta quantas letras escolhidas contem em uma palavra digitada pelo usuário

word = list(str(input()))
letter = str(input())
contagem = word.count(letter)
print(contagem)