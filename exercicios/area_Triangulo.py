#Funcao que retorna a area de um triangulo **retangulo**, recebendo como base um valor "a", e um valor "b" correspondendo a base e a altura do triangulo

def calc_area_Triangulo(a, b):  
    #cria uma variável que armazena o valor do calculo do triangulo retangulo 
    areaT = (a*b)/2
    return areaT


a = float(input('Insira o valor do lado do triangulo'))
b = float(input('Insira o valor da altura do triangulo'))

area_triangulo = calc_area_Triangulo(a, b)     #Chamando a função "calc_area_Triangulo" para realizar o calculo.
print(area_triangulo)                          #Exibe na tela o valor da área