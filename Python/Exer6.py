def converter_quilometros_para_metros(quilometros):
 #Vai fazer o calculo em metros
 metros = quilometros * 1000
 return metros

try:

    #Vai pedir para digitar a distancia em KM
    quilometros = float(input("Digite a distância em quilômetros: "))

    #Vai Converter a função converter_quilometros_para_metros para metros
    metros = converter_quilometros_para_metros(quilometros)
    print("metros:", metros)

#Se errar vai aparecer isso aq
except ValueError:

    print("Entrada inválida!")