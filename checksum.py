# Checksum
def Checksum_gen(dataword, word_size, num_blocks):
    checksum = ""
    if(word_size < 5):
        print("Your length of dataword is not the same as word size")
    else:
        raw_data = list(map(str, dataword.strip().split()))[:num_blocks] 
        print("Input Dataword - ", raw_data)
        # Separate dataword
        data = list(map(str, dataword.strip().split()))[:num_blocks] 
        for i in range(0, len(data)):
            if(len(data[i]) < word_size):
                fill = data[i].zfill(word_size)
                data[i] = fill  
        print("Dataword - ", data)
        print("Input Word size: ", word_size)
        print("Input Numblock: ", num_blocks)
        con_zero = '0' * word_size # 00000000... (len(word_size))
        # Calculatethe binary
        for i in data:
            # Ref: https://www.geeksforgeeks.org/python-program-to-add-two-binary-numbers/
            con_zero = bin(int(con_zero, 2) + int(i, 2))
        # Ref: https://docs.python.org/3/tutorial/introduction.html
        # characters from position 2 (included) to the end
        # Carry number from compute previous digit
        carry_number = con_zero[0]
        con_zero = con_zero[2:]
        con_zero = bin(int(con_zero, 2) + int(carry_number, 2))
        a = len(con_zero) - word_size
        con_zero = con_zero[a:]
        # Calculate the complement of sum (0 => 1, 1 => 0)
        for j in con_zero:
            if(j == '1'):
                checksum += '0'
            else:
                checksum += '1'
        print("1's compliment: ", checksum)
    return checksum
def Checksum_check(dataword, word_size, num_blocks, checksum):
    # Separate dataword
    data = list(map(str, dataword.strip().split()))[:num_blocks] 
    for i in range(0, len(data)):
        if(len(data[i]) < word_size):
            fill = data[i].zfill(word_size)
            data[i] = fill  
    li =list(checksum.split(" "))
    codeword = data + li
    print("\nInput codeword: ",codeword)
    con_zero = '0' * word_size
    for i in codeword:
        con_zero = bin(int(i, 2) + int(con_zero, 2))
    print("Receiver summation of binary number: ",con_zero[2:])
    carry_number = con_zero[:len(con_zero) - word_size]
    con_zero = con_zero[len(con_zero) - word_size:]
    con_zero = bin(int(con_zero, 2) + int(carry_number[:1], 2))
    con_zero = con_zero[2:]
    # Calculate the complement of sum (0 => 1, 1 => 0)
    compliment = ""
    for j in con_zero:
        if(j == '1'):
            compliment += '0'
        else:
            checksum += '1'
    print("1's compliment: ", compliment)
    count_zero = '0' * word_size
    # PASS=1 or FAIL=0
    # Returns '0' for '1' and '1' for '0'
    # Ref: https://www.geeksforgeeks.org/1s-2s-complement-binary-number/
    if(compliment == count_zero):
        print("PASS")
        return 1
    else:
        print(compliment)
        print("FAIL")
        return 0

################### MAIN ###################
# Checksum (Generator)
# dataword = input('Input Dataword: ')
# word_sizeG = int(input('Input Word Size: '))
# num_blocksG = int(input('Input Num Blocks: '))
# codeword = Checksum_gen(dataword, word_sizeG, num_blocksG)

# Checksum (Checker)
# codeword = input('Input Codeword: ')
# word_sizeC = int(input('Input Word Size: '))
# num_blocksC = int(input('Input Num Blocks: '))
# checksum = input('Input Check Sum: ')
# validity = Checksum_check(codeword, word_sizeC, num_blocksC, checksum)
############################################

