target_hex = "25393f33080c563b242200422f276327293616442c353a0e211c6c2f443e1e38035900474c3d"
output = bytes.fromhex(target_hex)
keys = [
    "KPMG H@ckademy".encode('utf-8'),
    "Can you find a flag? You need to REVERSE the code first!".encode('utf-8'),
    "KPMG{Level_1_fl@g_ther3_r_moor_to_find!}".encode('utf-8')
]

for key in keys:
    input_bytes = bytearray(len(output))
    for b in range(len(output)):
        input_bytes[len(output)-1-b] = output[len(output)-1-b] ^ key[b % len(key)]
    print(f"\nKey: {key.decode('utf-8')}")
    print("Raw input bytes (hex):", input_bytes.hex())
    try:
        flag = input_bytes.decode('utf-8')
        print("Recovered flag (UTF-8):", flag)
    except UnicodeDecodeError:
        print("Failed to decode as UTF-8")
    flag = input_bytes.decode('latin-1')
    print("Recovered flag (Latin-1):", flag)
    printable = ''.join(c if c.isprintable() else '.' for c in flag)
    print("Printable characters:", printable)
