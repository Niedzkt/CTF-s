import base64

# Zaszyfrowany ciąg Base64
enc_password = "0Nv32PTwgYjzg9/8j5TbmvPd3e7WhtWWyuPsyO76/Y+U193E"

# Klucz używany do XOR
key = b"armando"

# Dekodowanie Base64
decoded = base64.b64decode(enc_password)

# XOR deszyfrowanie
decrypted = bytearray(len(decoded))

for i in range(len(decoded)):
    decrypted[i] = decoded[i] ^ key[i % len(key)] ^ 0xDF

# Wypisanie odszyfrowanego hasła
print("Odszyfrowane hasło:", decrypted.decode(errors="ignore"))
