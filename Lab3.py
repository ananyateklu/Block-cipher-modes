
import math as m

def main():
    # get key and plaintext from user
    plaintext = input("Enter plaintext ")
    
    key = "a5Z#\t"
    # to encrypt and decrypt in ecb mode: 
    # ciphertext = ecb_mode(plaintext, key)
    # print(ciphertext)
    # ecb_mode_decrypt(ciphertext, key)


    # to encrypt and decrypt in cbc mode:
    blocks = [] 
    encoded_blocks = []
    blocks = to_blocks(plaintext)
    cbc_mode([1,0,1,0,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0], blocks, key, encoded_blocks)
    ciphertext = encoded_blocks
    cbc_mode_decryption([1,0,1,0,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0], ciphertext, key, encoded_blocks)
    
    
    
    # blocks = to_blocks(plaintext)
    
    # cfb_mode([1,0,1,0,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0], blocks, key, encoded_blocks)
    # blocks = to_blocks(plaintext)
    # encoded_blocks = []
    # ofb_mode([1,0,1,0,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0], blocks, key, encoded_blocks)
    # blocks = to_blocks(plaintext)
    # encoded_blocks = []
    # IV=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    # ctr_mode(IV,blocks,key,encoded_blocks,0)
    # ctr_mode([1,0,1,0,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,0,],blocks,key,encoded_blocks,[0,0,0,0,0,0,0,0,0,0])
def printResult(plain_text):
    result = '' 
    for i in range(0, len(plain_text)):
        if '\x00' in plain_text[i]:
            plain_text[i].replace('\x00', '')
        result += plain_text[i]
        if i%10 == 0:
            plain_text[i] = plain_text[i]+"\n"
    print (result)



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

# splits binary to groups of 7
def SplitBinary(binaryList):
    binary_combined = ""
    for i in binaryList:
        binary_combined += str(i)
    split_binary = " ".join(binary_combined[i:i+7] for i in range(0, len(binary_combined), 7))  
    return split_binary

# takes in a grouped of 7 binary to text
def binary_to_text(groupedbinary):
    ascii_string = ""
    for i in groupedbinary.split():
        an_integer = int(i,2)
        ascii_character = chr(an_integer)
        ascii_string += ascii_character
    return ascii_string

    
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
        xor_bits.append((int(binary_shift[i])+binary_key[i])%2)
    return xor_bits


def decode(cipherblock,key,plain_text):
    # convert key to binary
    binary_key = convert_bin(key)
     # add key mod 2
    xor_bits = []
    
    for i in range(0, len(binary_key)):
        xor_bits.insert(i,(cipherblock[i] + binary_key[i])%2)
    # shift the cipher block three to the left (reverse diffusion)
    binary_reverse_shift = []
    for i in range(0,len(cipherblock)):
        binary_reverse_shift.insert((i-3)%35, xor_bits[i]) 
    # change the binary list into a group of 7 bits 
    split_binary = SplitBinary(binary_reverse_shift)
   
    ascii_string = binary_to_text(split_binary)    

    plain_text.append(ascii_string)
    return binary_reverse_shift
    
    
def bin_to_blocks(binary_text):
    block_size = 35
    block_list = []
    # Check to see if text is already 35 bits
    if (len(binary_text) == block_size):
        block_list.insert(0, binary_text)
        return block_list
    # if not, divide into 35 bit blocks
    block_count = m.ceil(len(binary_text)/35)
    count = 0
    while(count < block_count):
        block = []
        for i in range(0,35):
            if (len(binary_text) > (35*count)+i):
                block.insert(i,int(binary_text[(35*count)+i])) 
            else:
                block.append(0)
        block_list.insert(count, block)
        count = count+1
    return block_list

def to_blocks(plaintext):
    block_size = 35
    block_list = []
    #convert plaintext to binary
    binary_text = convert_bin(plaintext)
    # Check to see if text is already 35 bits
    if (len(binary_text) == block_size):
        block_list.insert(0, binary_text)
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

def print_ciphertext(encoded_blocks, modes):
    result_str = ""
    for i in range(0, len(encoded_blocks)):
        result = str(encoded_blocks[i])
        punc = ''', '''
        result = result.replace(punc, "")
        result = result[1:36]
        print('{}'.format(modes))
        for j in range(0,5):
            print (result[(j*7):((j+1)*7)], end = " ")
            result_str += result[(j*7):((j+1)*7)] + " "
        print("")
    return result_str

def ecb_mode(plaintext, key,):
    blocks = [] 
    # convert plaintext to blocks of binary
    blocks = to_blocks(plaintext)
    # encode blocks
    encoded_blocks = []
    for i in range(0,len(blocks)):
        encoded_blocks.insert(i,encode(blocks[i],key))
    # Print ciphertext to user
    print_ciphertext(encoded_blocks, ' ecb_mode')
    return encoded_blocks

def ecb_mode_decrypt(ciphertext,key):
    ciphertext = str(ciphertext)
    punc = ''', '''
    ciphertext = ciphertext.replace(punc, "")
    ciphertext = ciphertext.replace("[", '')
    ciphertext = ciphertext.replace("]", '')
    blocks = []
    blocks = bin_to_blocks(ciphertext)
    
    plain = []
    for i in range(0, len(blocks)):
        decode(blocks[i],key,plain)
        
    printResult(plain)
    return plain

def cbc_mode(IV, blocks, key, encoded_blocks):
    # cipher_text = []
    # xor plaintext and IV
    xor_bits = [] 
    plain_text = blocks[0]
    for i in range(0,len(plain_text)):
        xor_bits.append((plain_text[i]+ IV[i])%2)
    # encode xor_bits and key
    ciphertext = encode(xor_bits,key)
    encoded_blocks.append(ciphertext)  # THIS MAY BE YOUR PROBLEM
    blocks.pop(0)
    # Call recursivly if more blocks remain
    length = len(blocks)
    # Print results if done
    if length == 0:
        print_ciphertext(encoded_blocks, 'cbc_mode')
        return encoded_blocks
    else:
        cbc_mode(ciphertext, blocks, key, encoded_blocks)  

def cbc_mode_decryption(IV, blocks, key, encoded_blocks):   
   # xor result wtih the IV
    for i in range(0, len(blocks)):
        ciphertext = blocks[i]
        filler =[] # just need to fill in arguement of decode 
        decoded_bits = decode(ciphertext, key, filler)
        xor_bits = [] 
        for j in range(0,len(IV)):
            xor_bits.append((decoded_bits[j]+IV[j])%2)
        # add xor_bits to result as plain text
        encoded_blocks.append(xor_bits)
        IV = ciphertext
    groups = print_ciphertext(encoded_blocks, ' cbc_mode_decryption')
    text = binary_to_text(groups)
    print(text)
def cfb_mode(IV, blocks, key, encoded_blocks):
    xor_bits = []
    # encode IV and key
    xor_bits = encode(IV, key)
    # xor result with plaintext
    plain_text = blocks[0]
    xor_bits = []
    for i in range(0, len(plain_text)):
        xor_bits.append((plain_text[i]+ IV[i])%2)
    # add to result
    encoded_blocks.insert(0, xor_bits)
    blocks.pop(0)
    # encode xor_bits and key
    # Call recursivly if more blocks remain
    length = len(blocks)
    # Print results if done
    if length == 0:
        print_ciphertext(encoded_blocks, ' cfb_mode')
    else:
        cfb_mode(xor_bits, blocks, key, encoded_blocks) 

def ofb_mode(IV, blocks, key, encoded_blocks):
    xor_bits = []
    # encode IV and key
    # xor reult with plaintext
    xor_IV_key = encode(IV,key)
    plain_text = blocks[0]
    for i in range(0, len(plain_text)):
        xor_bits.append((plain_text[i]+ IV[i])%2)
    # add to result
    encoded_blocks.insert(0, xor_bits)
    blocks.pop(0)
    # encode xor_bits and key
    if len(blocks) == 0:
        print_ciphertext(encoded_blocks, ' ofb_mode')        
    else:
        ofb_mode(xor_IV_key,blocks, key, encoded_blocks)
    # Call resursively if more blocks remain
        
    

def ctr_mode(IV,blocks,key, encoded_blocks,count):
    # convert IV to string for use later
    tempIV = str(IV)
    punc = ''', '''
    tempIV = tempIV.replace(punc, "")[1:20]
    # iv is 19 bits
    # counter is 16 bits
    # generate iv/counter combo for round
    bin_count = bin(count).replace('0b','') 
    # make sure counter is 16 bits
    if(len(bin_count)<16):
        padlen = (16 - len(bin_count))
        pad_str = '0'*padlen
        pad_str = str(pad_str) + bin_count
    else: 
        pad_str = str(bin_count)   
        # combine 16 bit counter and 19 bit IV
    combo_key = tempIV + pad_str
        # encode key and combo_key in block cipher
    encoded_block = encode(combo_key, key)
        # xor with plaintext
    xor_bits = []
    plain_text = blocks[0]
    for i in range(0, len(plain_text)):
        xor_bits.append((encoded_block[i]+ plain_text[i]) %2)
    encoded_blocks.insert(0, xor_bits)
    count = count +1
    blocks.pop(0)
    if len(blocks) == 0:
        print_ciphertext(encoded_blocks, ' ctr_mode')         
    else:
        ctr_mode(IV,blocks,key, encoded_blocks,count)
    
    


main()
