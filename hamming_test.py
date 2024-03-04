# Hamming Testcases
import hamming

def print_gen(dataword):
    result = hamming.Hamming_gen(dataword)
    print("Input Dataword: " + dataword)
    print("Codeword: " + result)
    print()

def print_check(codeword):
    err = hamming.Hamming_check(codeword)
    print("Input Codeword: " + codeword)
    print("Error at position:", err)
    print()    

# Generator
print('Hamming Code Generator Test Cases')
testG1 = print_gen('0110')
testG2 = print_gen('1001101')
testG3 = print_gen('1001101')
testG4 = print_gen('1100110')
testG5 = print_gen('111011')
testG6 = print_gen('0101010')
testG7 = print_gen('0001100')
testG8 = print_gen('0010101')
testG9 = print_gen('1110010')
testG10 = print_gen('1010000')

# Checker
print('Hamming Code Checker Test Cases')
testC1 = print_check('10010100101')
testC2 = print_check('001100110')
testC3 = print_check('00010101101')
testC4 = print_check('01100101000')
testC5 = print_check('11100110010')
testC6 = print_check('10010100101')
testC7 = print_check('10011100111') 
testC8 = print_check('10101010100')
testC9 = print_check('00110101101') 
testC10 = print_check('001011100')
