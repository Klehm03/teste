numeros = []
for i in range(10):
    try:
        numero = int(input("Digite um número inteiro: "))
        numeros.append(numero)
        #caso não for um número
    except ValueError:
        print("Entrada inválida!!!")
        continue  # pular para a próxima iteração
if len(numeros) > 0:
    soma = sum(numeros)
    media = soma / len(numeros)
    print("Soma:", soma)
    print("Média:", media)
else:
    print("Nenhum número válido foi digitado!")