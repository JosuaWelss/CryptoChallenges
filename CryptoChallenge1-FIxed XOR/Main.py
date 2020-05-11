def XOR(string1, string2):
    b1 = int(string1, 16)
    b2 = int(string2, 16)

    print(b1)
    print(b2)

    xor = b1 ^ b2

    print(hex(xor)[2:])





if __name__ == '__main__':
    string1 = '1c0111001f010100061a024b53535009181c'
    string2 = '686974207468652062756c6c277320657965'

    XOR(string1, string2)
