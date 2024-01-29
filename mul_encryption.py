# Multiplicative encryption
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
plantext = input("plan text: ").upper()
key = int(input("key: "))
ciphertext = ''
for i in range(len(plantext)):
    char = plantext[i]
    index = alpha.find(char)
    index = (index*key)%26
    ciphertext +=alpha[index]
print(f"cipher text: {ciphertext}")
