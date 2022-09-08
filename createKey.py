from Crypto import Random
from Crypto.PublicKey import RSA


random_generator = Random.new().read
rsa = RSA.generate(1024, random_generator)

ClavePrivada = rsa.exportKey()
with open('ClavePrivada.txt', 'wb') as file:
    file.write(ClavePrivada)

ClavePublica = rsa.publickey().exportKey()
with open('ClavePublica.txt', 'wb') as file:
    file.write(ClavePublica)

print("Se crearon las llaves correctamente")
print("Llave privada ", ClavePrivada)
print("Llave publica ", ClavePublica)