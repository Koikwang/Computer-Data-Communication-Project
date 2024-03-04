import parity 
# Test cases
# parity_gen(dataword, word_size, parity_type, array_size)
# parity_check(codeword, parity_type)

# one-dimensional-even
test_case_1  = parity.parity_gen("101101 110010 000 001111 11111", 6, 1, 5)
parity.parity_check(test_case_1, 1)
print("\n")
test_case_11 = parity.parity_gen("11011 001100 1010 010101", 6, 1, 4)
parity.parity_check(test_case_11, 1)
print("\n")

# one-dimensional-odd
test_case_2  = parity.parity_gen("1101 11010 1000 00111 11111", 8, 2, 5)
parity.parity_check(test_case_2, 2)
print("\n")
test_case_21 = parity.parity_gen("11001 1100 101010 01101", 6, 2, 4)
parity.parity_check(test_case_21, 2)
print("\n")

# two-dimensional-even
test_case_3  = parity.parity_gen("101101 110 1000 111 11111111 11 001 010", 8, 3, 8)
parity.parity_check(test_case_3, 3)
print("\n")
test_case_31 = parity.parity_gen("11011 00100 10010 01001", 7, 3, 4)
parity.parity_check(test_case_31, 3)
print("\n")
test_case_32 = parity.parity_gen("1110 1100 00111 100001", 6, 3, 4)
parity.parity_check(test_case_32, 3)
print("\n")

# two-dimensional-odd
test_case_4  = parity.parity_gen("101101 110010 10000 001111 11111", 6, 4, 5)
parity.parity_check(test_case_4, 4)
print("\n")
test_case_41 = parity.parity_gen("11011 001100 1010 01001", 7, 4, 4)
parity.parity_check(test_case_41, 4)
print("\n")
test_case_42 = parity.parity_gen("111000 10100 0001 100", 9, 4, 4)
parity.parity_check(test_case_42, 4)
print("\n")

