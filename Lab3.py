
import math as m

def main():
    # get key and plaintext from user
    plaintext = input("Enter plaintext ")
    key = "a5Z#\t"
    print(key)
    blocks = [] 
    # convert plain to blocks of binary
    blocks = to_blocks(plaintext)
    # encode blocks
    #encode(plaintext, "a5Z#\t")
    ecb_mode(plaintext, key,)
    

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
    # convert key to binary
    binary_key = convert_bin(key)
    # shift the plaintext three to the right
    binary_shift = [] 
    for i in range(0, len(plaintext)):
        binary_shift.insert((i+3)%35,plaintext[i]) 
    # add key mod 2
    xor_bits = []
    for i in range(0, len(binary_key)):
        xor_bits.append((binary_shift[i]+binary_key[i])%2)
    return xor_bits

def to_blocks(plaintext):
    block_size = 35
    block_list = []
    #convert plaintext to binary
    binary_text = convert_bin(plaintext)
    # Check to see if text is already 35 bits
    if (len(binary_text) == block_size):
        block_list.insert(0, binary_text)
        print("rightSize")
        return block_list
    # if not, divide into 35 bit blocks
    block_count = m.ceil(len(binary_text)/35)
    count = 0
    while(count < block_count):
        block = []
        for i in range(0,35):
            if (len(binary_text) > (35*count)+i):
                block.insert(i,binary_text[(35*count)+i]) 
            else:
                block.append(0)
        block_list.insert(count, block)
        count = count+1
    return block_list

def print_ciphertext(encoded_blocks):
    for i in range(0, len(encoded_blocks)):
        result = str(encoded_blocks[i])
        punc = ''', '''
        result = result.replace(punc, "")
        result = result[1:36]
        print(result)
        for j in range(0,5):
            print (result[(j*7):((j+1)*7)], end = " ")


def ecb_mode(plaintext, key,):
    blocks = [] 
    # convert plaintext to blocks of binary
    blocks = to_blocks(plaintext)
    # encode blocks
    encoded_blocks = []
    for i in range(0,len(blocks)):
        encoded_blocks.insert(i,encode(blocks[i],key))
    # Print ciphertext to user
    print_ciphertext(encoded_blocks)
            
        






    

main()
#def decrypt(ciphertext, key):