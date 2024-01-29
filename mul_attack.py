# Multiplicative attack
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ciphertext = input("cipher text: ").upper()
plantext = ''
for k in range(1,26,2):
    if k ==13:
        continue
    for i in range(1,26,2):
        if i==13:
            continue
        if k*i %26==1:
            keyinverse = i
            break
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        index = alpha.find(char)
        index = (index*keyinverse)%26
        plantext +=alpha[index]
    print(f"at key:{k} & k_inverse:{keyinverse} -> plan text: {plantext}")
    plantext = ''
