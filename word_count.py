
with open('lorem_ipsum.txt','r') as file:
    texto   =   (file.read())
    texto   =   str.lower(texto)

    texto   =   (texto.split())
    print       (texto)
    
     # for i in range(texto):

               
frecuencia = [texto.count(w) for w in texto]
print (frecuencia)
print (len(frecuencia))
print       (len(texto))
print("Pares\n" + str(list(zip(texto, frecuencia))))

