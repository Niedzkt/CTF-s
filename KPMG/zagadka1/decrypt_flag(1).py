from hashlib import sha256
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# DH parameters from chat.txt
A = 8370337962458643162004582468469045984889816058567658904788530882468973454873284491037710219222503893094363658486261941098330951794393018216763327572119677
B = 9755909033513767641159594933585734179714892615169429957597029280980531443144704341694474385957669949989090202320232433789032328934018623049865998847328154
p = 10332921861938291919377635159012636040519117927041835671194203494937679183911345052843111512544303969800681115505917911462916407940308340306260755239268943
g = 577

# Compute shared secret (flawed DH using XOR)
S = (g ^ A ^ B) % p
shared_secret = str(S)

# Encrypted flag
ciphertext = "UYaG0KR+k8SmDn9ag/LV9u8h76iXpy6n5D7u00Y3rU/+suuGWSvm6J1ajXO2HxGgt6gyDFtNUZnsgfxGBAysGg=="

# Derive AES key
key = sha256(shared_secret.encode('utf-8')).digest()

# Decode ciphertext
raw = b64decode(ciphertext)
iv = raw[:AES.block_size]
encrypted_data = raw[AES.block_size:]

# Decrypt
cipher = AES.new(key, AES.MODE_CBC, iv)
try:
    decrypted = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    print("Decrypted flag:", decrypted.decode('utf-8'))
except Exception as e:
    print("Decryption failed:", e)
