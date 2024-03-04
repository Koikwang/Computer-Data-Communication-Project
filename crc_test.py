# CRC Testcases
import crc

def print_gen(dataword, word_size, CRC_type):
    result = crc.CRC_gen(dataword, word_size, CRC_type)
    print("Input Dataword: " + dataword)
    print("Input Word Size: " + str(word_size))
    print("Input CRC Type: " + CRC_type)
    print("Codeword: " + result)
    print()

def print_check(codeword, CRC_type):
    valid = crc.CRC_check(codeword, CRC_type)
    print("Input Codeword: " + codeword)
    print("Input CRC Type: " + CRC_type)
    print("Validation:", valid)
    print()   

# Generator
print('CRC Code Generator Test Cases')    
testG1 = print_gen('1101', 5, 'CRC-4')
testG2 = print_gen('1100001', 5, 'CRC-8')
testG3 = print_gen('11001101', 5, 'Reversed CRC-16')
testG4 = print_gen('1110010', 5, 'CRC-16')
testG5 = print_gen('0111110', 5, 'CRC-32')
testG6 = print_gen('111010110', 5, 'Reversed CRC-16')
testG7 = print_gen('1001', 5, 'CRC-4')
testG8 = print_gen('1101111', 8, 'CRC-16')
testG9 = print_gen('1001011', 5, 'CRC-8')
testG10 = print_gen('111011101', 5, 'CRC-4')

# Checker
print('CRC Code Checker Test Cases')
testC1 = print_check('110001100', 'CRC-4')
testC2 = print_check('011011110000000101100010', 'CRC-16')
testC3 = print_check('0111001111101', 'CRC-8')
testC4 = print_check('11001100110011', 'CRC-8')
testC5 = print_check('110011000000001010101000', 'CRC-16')
testC6 = print_check('11001101', 'CRC-4')
testC7 = print_check('0110011110110010111000101001011010010010000', 'CRC-32')
testC8 = print_check('10001111', 'CRC-4')
testC9 = print_check('010111011000000111001101', 'CRC-16')
testC10 = print_check('1110011111011011111011100111011001111100', 'CRC-32')