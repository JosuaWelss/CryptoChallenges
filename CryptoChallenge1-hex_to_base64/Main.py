import base64
import codecs


def hex_to_b64():

    hex = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    b = bytes.fromhex(hex)

    x = base64.standard_b64encode(b)
    print(x)




if __name__ == '__main__':
    hex_to_b64()