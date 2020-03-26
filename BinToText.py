
print(bytearray.fromhex(hex(int('110100001100101011011000110110001101111', 2))[2:]).decode())

print(bin(int('hello'.encode('utf-8').hex(), 16))[2:])
