import random
import string

chars = " "+string.punctuation +string.digits + string.ascii_letters

chars = list(chars)
#print(chars)
key = chars.copy()

random.shuffle(key)

# print(f"Chars: {chars}")
# print(f"Keys: {key}")

# encrypt

plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    char_index=chars.index(letter)
    cipher_text += key[char_index]

print(f"The Encrypted text is: {cipher_text}")

# decrypt

cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    char_index=key.index(letter)
    plain_text += chars[char_index]

print(f"The Decrypted text is: {plain_text}")