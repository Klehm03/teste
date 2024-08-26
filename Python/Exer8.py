def dobrar_lista(lista):
  nova_lista = []
  for elemento in lista:
    novo_elemento = elemento * 2
    nova_lista.append(novo_elemento)
  return nova_lista  # Retorno fora do loop

lista = []  # Inicio da lista vazia
i = 1
while i <= 10:
  elem = int(input("Digite um elemento da lista: "))
  lista.append(elem)
  i += 1

print("Original:", lista)
nova_lista = dobrar_lista(lista)
print("Dobrada:", nova_lista)