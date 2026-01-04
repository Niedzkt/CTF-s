target = bytes.fromhex("25393f33080c563b242200422f276327293616442c353a0e211c6c2f443e1e38035900474c3d")
key = "_encrypted_password".encode()  # Klucz: KPMG H@ckademy
flag = bytearray(len(target))
for b in range(len(target)):
    i = len(target) - b - 1
    flag[i] = target[i] ^ key[b % len(key)]
try:
    print("Flaga:", flag.decode())
except UnicodeDecodeError:
    print("Nie udało się zdekodować. Wynik w hex:", flag.hex())
