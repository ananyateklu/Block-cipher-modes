def main():
    plaintext = input("Enter plaintext")
    for ch in plaintext:
        decimal = []
        decimal[ch] = ord(plaintext[ch])
        print(plaintext)
