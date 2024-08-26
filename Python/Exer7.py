def maior_menor(lista):
 maior = lista[0]
 menor = lista[0]

 #Laço para ficar comparando
 for elemento in lista:
  if elemento > maior:
   maior = elemento
  elif elemento < menor:
   menor = elemento
 return maior, menor
lista=list()
i=1

#Vai guardar e mostrar os numeros armazenados na lista
while i<=10:
 elem = int(input("Digite um elemento da lista:"))
 lista.append(elem)
 i+=1
 print(lista)
 
 #Mostra os maior e o menor 
maior, menor = maior_menor(lista)
print("Maior:", maior)
print("Menor:", menor)