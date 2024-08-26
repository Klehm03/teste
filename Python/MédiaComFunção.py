def lernotas():
    n=float(input('Digite uma nota para o aluno(a): '))
    return n


def resultado(n1,n2, n3, n4):
    media=(n1+n2+n3)/4
    print("Nota 1: ", n1)
    print("Nota 2: ", n2)
    print("Nota 3: ", n3)
    print("Nota 4: ", n4)
    print("Média: ", media, "\nResultdo: ", end="")
    if media >= 7:
        print(" Aprovado")
    else: 
        print(" Reprovado")


a = lernotas()
b = lernotas()
c = lernotas()
d = lernotas()
resultado(a,b, c, d)