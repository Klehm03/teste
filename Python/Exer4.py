#Declara a função
def maior3(a, b, c):
 #Se o número da variavel A for maior ou igual ao número da variavel b e maior ou igual a c, ele vai retornar A, e assim acontece
 #até no fim do else
 if a >= b and a >= c:
    return a
 elif b >= c:
    return b
 else: return c

n1=int(input("Digite um número:"))
n2=int(input("Digite um número:"))
n3=int(input("Digite um número:"))
#Vai comparar e vai passar o maior para a variavel resultado
resultado = maior3(n1,n2,n3)
print(resultado)