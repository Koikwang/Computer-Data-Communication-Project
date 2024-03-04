# Cyclic Redundancy Check (CRC)

# XOR function 
# 0 xor 0 -> 0
# 0 xor 1 -> 1
# 1 xor 0 -> 1
# 1 xor 1 -> 0
def xor(dividend, divisor):
    result = ''
    i = 1
    while i < len(dividend):
        if dividend[i] == divisor[i]:
            result += '0'
        else:
            result += '1'
        i += 1
    return result          

# Find divisor bit depend on CRC Type
def divisor(CRC_type) :
    div = ''
    if CRC_type == "CRC-4":
        div = '11111' # 5 bits
    elif CRC_type == "CRC-8":    
        div = '111010101' # 9 bits
    elif CRC_type == "CRC-16":
        div = '11000000000000101' # 17 bits
    elif CRC_type == "CRC-24":
        div = '1100000000101000100000001' # 25 bits      
    elif CRC_type == "CRC-32":
        div = '100000100110000010001110110110111' # 33 bits    
    elif CRC_type == "Reversed CRC-16":  
        div = '10100000000000011' # 17 bits 
    return div

# Solve CRC problem by modulo2 division function
def modulo_2(divisor, dividend):
    p = len(divisor)  # Divisor length
    n = len(dividend) # Dividend length
    selected_dividend = dividend[0:p] # Select the first dividend range from 0 to divisor length

    while p < n:
        if selected_dividend[0] == '1':
            selected_dividend = xor(selected_dividend, divisor) + dividend[p]
        else:
            selected_dividend = xor(selected_dividend, '0' * p) + dividend[p]   
        p += 1
    # Last bit in dividend
    if selected_dividend[n-p] == '1':
        selected_dividend = xor(selected_dividend, divisor)
    else:
        selected_dividend = xor(selected_dividend, '0' * p);    
    return selected_dividend
    
# CRC Generator
def CRC_gen(dataword, word_size, CRC_type):
    # If dataword size less than word size append zero at the beginning of dataword
    if len(dataword) < word_size: 
        dataword = ('0' * (word_size-len(dataword))) + dataword 

    div = divisor(CRC_type)       # Divisor according to CRC Type
    extra_bit = len(div) - 1      # Extra bits length = divisor - 1

    # Add extra bit into dataword become a dividend
    dividend = dataword + ('0' * extra_bit) # Dividend
    # print(dividend)
    # Solve CRC problem
    result = modulo_2(div, dividend)

    return dataword + result
    
# CRC Checker
def CRC_check(codeword, CRC_type):
    div = divisor(CRC_type)          # Divisor according to CRC Type
    valid = modulo_2(div, codeword)  # Solve CRC problem
    
    return 'PASS' if int(valid) == 0 else 'FAIL'

################### MAIN ###################
# CRC (Generator)
# dataword = input('Input Dataword: ') 
# word_size = int(input('Input Word Size: ')) 
# CRC_type = input('Input CRC-type: ')
# codeword = CRC_gen(dataword, word_size, CRC_type)
# print("Codeword: " + codeword)

# CRC (Checker)
# codeword = input('Input Codeword: ')
# CRC_type = input('Input CRC-type: ')
# validity = CRC_check(codeword, CRC_type)
# print("Validation:", validity)
#############################################

# References
# https://www.geeksforgeeks.org/modulo-2-binary-division/
