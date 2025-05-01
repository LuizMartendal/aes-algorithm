from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from main import AES as MY_AES

key = b'ABCDEFGHIJKLMNOP'
plaintext = b'DESENVOLVIMENTO!'

my_cipher = MY_AES('65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80')
ciphertext = my_cipher.encrypt(plaintext)

# Biblioteca oficial
lib_cipher = AES.new(key, AES.MODE_ECB)
decrypted = unpad(lib_cipher.decrypt(ciphertext), 16)

print("🔐 Decriptado com pycryptodome:", decrypted)
