import binascii
def main():
    plaintext = input("Enter plaintext")
    encode(plaintext, "a5Z#\t")

def convert_bin(acii):
    decimal_vals = []
    # Type cast plaintext to acii chars
    for i in range(0, len(acii)):
        decimal_vals.append(ord(acii[i]))
    # Type cast decimal to binary
    binary_text = []
    # convert the decimal values to one big array of binary 
    for i in range(0,len(decimal_vals)):
        conversion = bin(decimal_vals[i])
        conversion = conversion[2:]
        # accounting for padding if binary < 7 bits
        if(len(conversion)<7):
            padlen = 7-len(conversion)
            padstr = "0" * padlen
            conversion = padstr+conversion                
        for j in range(0,len(conversion)):
            binary_text.insert((7*i+j), int(conversion[j]))
    return binary_text


def encode(plaintext, key):
    # convert plaintext to binary
    binary_plain = convert_bin(plaintext)
    # convert key to binary
    binary_key = convert_bin(key)
    # shift the plaintext three to the right
    binary_shift = [] 
    for i in range(0, len(binary_plain)):
        binary_shift.insert((i+3)%35,binary_plain[i]) 
    # add key mod 2
    xor_bits = []
    for i in range(0, len(binary_key)):
        xor_bits.append((binary_shift[i]+binary_key[i])%2)
    return xor_bits
    

main()
#def decrypt(ciphertext, key):