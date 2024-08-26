def mdc(a, b):
 if b == 0:
    return a
 else:
    #Vai retornar o maximo divisor comum da função
    return mdc(b, a % b)
num1 = int(input("Digite um número:"))
num2 = int(input("Digite outro número:"))
#Vai colocar o resultado final do maximo divisor comum na variavel resultado
resultado = mdc(num1, num2)
print("MDC:", resultado)
