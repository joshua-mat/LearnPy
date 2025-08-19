from curses.ascii import isalpha


def encrypt_string(text):
    encrypted = []
    for c in text:
        if isalpha(c):
            if c.islower():
               x = chr((ord(c)-ord('a')+3) % 26 + ord('a'))
               encrypted.append(x)
            elif c.isupper():
                x = chr((ord(c)-ord('A')+3) % 26 + ord('A'))
                encrypted.append(x)
        else:
            encrypted.append(c)
    return ''.join(encrypted)


# Encrypt the string "Hello, Python!" by shifting each letter in the alphabet one by one.
encrypted_text = encrypt_string("Hello, Python!")
print("The encrypted text is:", encrypted_text)  # Should print out "Ifmmp, Qzuipo!"