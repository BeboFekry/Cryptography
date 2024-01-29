# affine attack
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
    for k2 in range(26):
        for i in range(len(ciphertext)):
            char = ciphertext[i]
            index = alpha.find(char)
            index = (index-k2)%26
            index = (index*keyinverse)%26
            plantext +=alpha[index]
        print(f"at key:{k} & key2:{k2} -> plan text: {plantext}")
        plantext = ''
