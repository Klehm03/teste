notaA=float(input("Informe a primeira nota: \n"))
notaB=float(input("Informe a segunda nota: \n"))

#calcular media
mediafinal = (notaA+notaB)/2

#verificação

if (mediafinal>=7.0):
    print("A Média: %.1f - APROVADO"% mediafinal);
elif 6.9 >= mediafinal >= 5.0:
    print("A Média: %.1f - EXAME"% mediafinal)
else:
    print("A Média: %.1f - REPROVADO"% mediafinal)
