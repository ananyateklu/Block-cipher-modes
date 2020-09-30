import binascii
def main():
    plaintext = input("Enter plaintext")
    encode(plaintext, "poop")




def encode(plaintext, key):
    decimal_vals = []
    # Type cast plaintext to acii chars
    for i in range(0, len(plaintext)):
        decimal_vals.append(ord(plaintext[i]))
    # Type cast decimal to binary
    binary_text = []
    conversion = '' 
    for i in range(0,len(decimal_vals)):
        conversion = bin(decimal_vals[i])
        conversion = conversion[2:]
        for j in range(0,len(conversion)):
            binary_text.insert((7*i+j), int(conversion[j]))
    print(binary_text)
    # for i in range(0, len(plaintext)):
    #     block[i] = plaintext[i+3%35]
    #     print(plaintext)


main()
#def decrypt(ciphertext, key):