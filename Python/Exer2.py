deslocamento = int(input("Digite o deslocamento")) 
texto = input("Digite o texto a ser criptografado: ")
texto_criptografado = ""
for letra in texto: 
 #Calcula a letra criptografada para letras Maiúsculas basicamente
 if letra.isupper(): letra_criptografada = chr((ord(letra.lower()) + deslocamento - 97) % 26 + 65)

 #Calcula a letra criptografada para Letras Minusulas 
 elif letra.islower():letra_criptografada = chr((ord(letra) + deslocamento - 97) % 26 + 97) 

 #Aqui é caso seja números, dai não modifica o caracter
 else: letra_criptografada = letra 
 texto_criptografado += letra_criptografada 
 
 #Mostra o Texto Criptografado
print("Texto criptografado:", texto_criptografado)