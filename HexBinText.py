def bin_to_hex(b):
    return hex(int(b, 2))[2:]


def hex_to_bin(hx):
    return bin(int(hx, 16))[2:]


def hex_to_text(hx):
    return bytearray.fromhex(hx).decode()


def text_to_hex(txt):
    return txt.encode('utf-8').hex()


def bin_to_text(b):
    return hex_to_text(bin_to_hex(b))


def text_to_bin(txt):
    return hex_to_bin(text_to_hex(txt))


print(bin_to_hex('11111111'))
print(hex_to_bin('ff'))

s = '68 65 78 61 64 65 63 69 6d 61 6c 20 6f 72 20 62 61 73 65 31 36 3f'

print(hex_to_text(s.replace(' ', '')))

print(text_to_hex('hello'))
print(hex_to_text('68656c6c6f'))

bin1 = '01101100 01100101 01110100 01110011 00100000 01110100 01110010 01111001 00100000 01110011 01101111 01101101 ' \
       '01100101 00100000 01100010 01101001 01101110 01100001 01110010 01111001 00100000 01101111 01110101 01110100 ' \
       '00100001 '
print(bin_to_text(bin1.replace(' ', '')))

print(text_to_bin('hello'))
print(bin_to_text('110100001100101011011000110110001101111'))

decstr = '85 110 112 97 99 107 32 116 104 105 115 32 66 67 68'
x = ''.join([hex(int(e))[2:] for e in decstr.split(' ')])
print(hex_to_text(x))
