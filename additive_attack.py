# additive attack
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ciphertext = input("cipher text: ").upper()
plantext = ''
for k in range(26):
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        index = alpha.find(char)
        index = (index-k)%26
        plantext +=alpha[index]
    print(f"at key: {k} -> plan text: {plantext}")
    plantext = ""
