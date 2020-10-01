import binascii
def main():
    plaintext = input("Enter plaintext ")
    print(encode(plaintext, "a5Z#\t"),"ciphertext")
    decode([0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1],"a5Z#\t")
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
        xor_bits.append((int(binary_shift[i])+ binary_key[i])%2)
    return xor_bits

def decode(cipherblock,key):
    # convert key to binary
    binary_key = convert_bin(key)
    # shift the cipher block three to the left(reverse diffusion)
    binary_reverse_shift = []
    for i in range(0,len(cipherblock)):
        binary_reverse_shift.insert((i-3)%35,cipherblock[i])
    print(binary_reverse_shift,"reversed")
    print(binary_key,"key")
    # add key mod 2
    xor_bits = []
    for i in range(0, len(binary_key)):
        xor_bits.insert(i,(binary_reverse_shift[i] + binary_key[i])%2)
    print(xor_bits,"xor")
    binary_combined = ""
    for i in xor_bits:
        binary_combined += str(i)
    split_binary = " ".join(binary_combined[i:i+7] for i in range(0, len(binary_combined), 7))  
    print(split_binary,"binary")
    ascii_string = ""
    for i in split_binary.split():
        an_integer = int(i,2)
        ascii_character = chr(an_integer)
        ascii_string += ascii_character
    print(ascii_string)
  


main()
#def decrypt(ciphertext, key):