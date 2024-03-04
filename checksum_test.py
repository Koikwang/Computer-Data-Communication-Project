import checksum
# Test cases
# Checksum_gen(dataword, word_size, num_blocks)
# Checksum_check(dataword, word_size, num_blocks, checksum)

test_case_1  = checksum.Checksum_gen("110011 11001110 1011101", 10, 3)
checksum.Checksum_check("110011 11001110 1011101", 10, 3, test_case_1)
print("\n")
test_case_2 = checksum.Checksum_gen("10011 01011 100", 6, 3)
checksum.Checksum_check("10011 01011 100", 6, 3, test_case_2)
print("\n")
test_case_3 = checksum.Checksum_gen("11011 00100 1 010101", 6, 4)
checksum.Checksum_check("11011 00100 1 010101", 6, 4, test_case_3)
print("\n")
test_case_4 = checksum.Checksum_gen("1101 10001 0001111 10011", 7, 4)
checksum.Checksum_check("1101 10001 0001111 10011", 7, 4, test_case_4)
print("\n")
test_case_5 = checksum.Checksum_gen("1010 0110 100110", 6, 3)
checksum.Checksum_check("1010 0110 100110", 6, 3, test_case_5)
print("\n")
test_case_6 = checksum.Checksum_gen("0101011 1011001 10010101111", 11, 3)
checksum.Checksum_check("0101011 1011001 10010101111", 11, 3, test_case_6)
print("\n")
test_case_7 = checksum.Checksum_gen("1011 11111 1001", 6, 3)
checksum.Checksum_check("1011 11111 1001", 6, 3, test_case_7)
print("\n")
test_case_8 = checksum.Checksum_gen("0011 11011 111000", 6, 3)
checksum.Checksum_check("0011 11011 111000", 6, 3, test_case_8)
print("\n")
test_case_9 = checksum.Checksum_gen("10100 0010010 1110010 1011001", 8, 4)
checksum.Checksum_check("10100 0010010 1110010 1011001", 8, 4, test_case_9)
print("\n")
test_case_10 = checksum.Checksum_gen("1010111 1111001", 8, 2)
checksum.Checksum_check("1010111 11111100", 8, 2, test_case_10)
print("\n")






