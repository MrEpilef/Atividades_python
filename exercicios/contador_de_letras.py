#Este algoritmo conta quantas letras, escolhida pelo usuário, existe em uma palavra inserida também por ele

def cont_letters_in_word(word, letter):

    contagem = word.count(letter)                           
        #utilizando do método ".count" para retornar quantas letras existem na palavra

    return contagem         #Imprimindo resultado

word = list(str(input('Digitre a palavra: ')))          
        #lendo a palavra do usuario

letter = str(input('Digite a letra a ser contada: '))   
        #Lendo qual etra o usuário quer contar na palava escolhida

letras=cont_letters_in_word(word, letter) #variavel recebendo o valor que a funcao retornara, passando como paramentro as variaveis "word" e "letter" 
print(letras)