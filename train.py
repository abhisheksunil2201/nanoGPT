with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# all the unique characters that occur in input.txt
chars = sorted(list(set(text)))
vocab_size = len(chars)

# mapping from characters to integers
stoi = { ch:i for i,ch in enumerate(chars) }
itos = { i:ch for i,ch in enumerate(chars) }
encode = lambda s: [stoi[c] for c in s] # encoder: take a string, output a list of integers
decode = lambda l: ''.join([itos[i] for i in l]) # decoder: take a list of integers, output a string

print(encode("hello abhishek"))
print(decode(encode("hello abhishek")))