target_hex = "25393f33080c563b242200422f276327293616442c353a0e211c6c2f443e1e38035900474c3d"
output = bytes.fromhex(target_hex)  # Convert hex to bytes
key = "KPMG{Level_1_fl@g_ther3_r_moor_to_find!}".encode('utf-8')  # Replace with actual resource string

input_bytes = bytearray(len(output))
for b in range(len(output)):
    input_bytes[len(output)-1-b] = output[len(output)-1-b] ^ key[b % len(key)]

flag = input_bytes.decode('utf-8')  # Try decoding as UTF-8
print(flag)
