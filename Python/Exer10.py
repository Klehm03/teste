def obter_ultimo_elemento(lista):
 if lista:
  
  #Lista vai sempre voltar um na variável
  return lista[-1]
 else: return None
lista=list()
i=1
    #Laço pra ir de 1 á 5
while i<=5:
  elem = int(input("Digite um elemento da lista:"))
  lista.append(elem)
  i+=1
  print(lista)
  ultimo_elemento = obter_ultimo_elemento(lista)
  print("Último elemento da lista: \n", ultimo_elemento)