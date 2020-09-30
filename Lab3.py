def main():
    plaintext = input("Enter plaintext")
    for i in range(0,len(plaintext)):
        decimal =[]
        decimal.append(ord(plaintext[i])) 
        print(decimal)


main()