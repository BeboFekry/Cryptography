# Alice affine question
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
plantext = input("plan text: ").upper()
key = int(input("key: "))
key2 = int(input("key2: "))
ciphertext = ''
for i in range(len(plantext)):
    char = plantext[i]
    index = alpha.find(char)
    index = (index*key)%36
    index = (index+key2)%36
    ciphertext +=alpha[index]
print(f"cipher text: {ciphertext}")
