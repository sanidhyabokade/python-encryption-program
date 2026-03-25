import random
import string

chars = " "+ string.punctuation + string.ascii_letters + string.digits;
chars = list(chars);
key = chars.copy();

random.shuffle(key);

plain_text = input("Enter a text for encryption: ");
cypher_text = "";

for letter in plain_text:
    index = chars.index(letter);
    cypher_text += key[index];

print(f"Orginal message is {plain_text}");
print(f"Encrypted message is {cypher_text}");