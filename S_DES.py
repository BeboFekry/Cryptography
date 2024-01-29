# S-DES

# encryption
def des_encrypt(plaintext, key):
    state = plaintext
    # subkey generation (scheduling) = generate 2 subkeys
    subkeys = generate_subkey(key)
    # initial permutation
    state = ip(state)
    # 2 fiestel networks
    for i in range(2):
        state = feistel(state, subkeys[i])
    # final permutation
    state = ip_1(state)
    ciphertext = state
    return ciphertext

def key_shift(key):
    k2 = ''
    for i in range(1,5):
        k2 += key[i]
    k2 += key[0]
    return k2

def generate_subkey(key):
    # P10
    key = p10(key)
    # split key
    key_l = key[:5]
    key_r = key[5:]
    # LS-1
    key_l_shifted = key_shift(key_l)
    key_r_shifted = key_shift(key_r)
    key = key_l_shifted + key_r_shifted
    # P8 --> subkey 0
    subkey_0 = p8(key)
    # split key2
    key_l = key[:5]
    key_r = key[5:]
    # LS-2 
    key_l_shifted = key_shift(key_l)
    key_r_shifted = key_shift(key_r)
    key = key_l_shifted + key_r_shifted
    # P8 --> subkey 1
    subkey_1 = p8(key)
    return subkey_0, subkey_1

def feistel(state, subkey):
    # split state
    state_l = state[:4]
    state_r = state[4:]
    # first round function
    f_state_r = round_function(state_r, subkey)
    # XOR right side with left side of the state
    # print(len(state_l), len(f_state_r))
    state_l = XOR(state_l, f_state_r)
    state = state_r + state_l
    return state

def round_function(state, subkey):
    output = ''
    # E/P (Expansion Permutation)
    state = e_p(state)
    # XOR with subkey
    state = XOR(state,subkey)
    # Sbox
    state = sbox(state)
    # P4
    state = p4(state)
    # return output
    return state

def XOR(n1,n2):
    out =''
    for i in range(len(n1)):
        if (n1[i] == n2[i]):
            out += '0'
        else:
            out += '1'
    return out

# === permutation & substitution functions === #
def p10(inp):
    output = ''
    P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]   
    # for i in range(10):
    for j in P10:
        output += inp[j-1]

    return output
def p8(inp):
    output = ''
    P8 = [6, 3, 7, 4, 8, 5, 10, 9]   

    # for i in range(10):
    for j in P8:
        output += inp[j-1]
    return output

def p4(inp):
    output = ''
    P4 = [2, 4, 3, 1]
    # for i in range(10):
    for j in P4:
        output += inp[j-1]
    return output
# IP (Initial Permuation)
def ip(inp):
    output = ''
    IP = [2, 6, 3, 1, 4, 8, 5, 7]
    for j in IP:
        output += inp[j-1]
    return output

# IP**-1 (Final Permutation)
def ip_1(inp):
    output = ''
    IP_1 = [4, 1, 3, 5, 7, 2, 8, 6]
    for j in IP_1:
        output += inp[j-1]
    return output

# E/P (Expansion Permutation)
def e_p(inp):
    out = ''
    E_P = [4, 1, 2, 3, 2, 3, 4, 1]
    for i in E_P:
        out += inp[i-1]
    return out

def sbox(inp):
    output = ''
    # split input
    input_0 = inp[:4]
    input_1 = inp[4:]
    # sboxes
    S0 = [['01', '11', '00', '11'], ['00', '10', '10', '01'], ['11', '01', '01', '11'], ['10', '00', '11', '10']]
    S1 = [['00', '10', '11', '10'], ['01', '00', '00', '01'], ['10', '01', '01', '00'], ['11', '11', '00', '11']]
    # substitution
    raw = input_0[0]+input_0[3]
    raw = binary_to_decimal(raw)
    col = input_0[1]+input_0[2]
    col = binary_to_decimal(col)
    out0 = S0[raw][col]

    raw = input_1[0]+input_1[3]
    raw = binary_to_decimal(raw)
    col = input_1[1]+input_1[2]
    col = binary_to_decimal(col)
    out1 = S1[raw][col]
    output = out0+out1
    return output

def binary_to_decimal(inp):
    decimal = 0
    index = -1
    for i in range(2):
        decimal += int(inp[index])*(2**i)
        index -=1
    return decimal
# ______________________________________________________________________

plaintext = input("Plaintext in binary: ")
key = input("Key in binary: ")
ciphertext = des_encrypt(plaintext,key)
print("Ciphertext:",ciphertext)