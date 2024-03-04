# Parity Bit
import numpy as np
# Define
one = "1"
zero = "0"
def parity_gen(dataword, word_size, parity_type, array_size):
    codeword = []
    # Type of parity that user want to use
    if(parity_type == 1):
        print("Your parity type is one-dimensional-even")
        if(word_size < 5): 
            print("Your word size should equal or more than 5")
        else:
            raw_data = list(map(str, dataword.strip().split()))[:array_size] 
            print("Input Dataword - ", raw_data)
            # Separate dataword
            data = list(map(str, dataword.strip().split()))[:array_size] 
            for i in range(0, len(data)):
                if(len(data[i]) < word_size):
                    fill = data[i].zfill(word_size)
                    data[i] = fill 
            # Input
            print("Input Dataword - ", data)
            print("Word size: ", word_size)
            print("Array size: ", array_size)
            for i in range(0,array_size):
                count_1 = data[i].count(one)
                new_data = ""
                new_data1 = ""
                if(word_size == len(data[i])):
                    if(count_1 % 2 == 0):
                        # Put 0 into the dataword
                        new_data = data[i] + '0'
                    if(count_1 % 2 == 1):
                        # Put 1 into the dataword
                        new_data1 = data[i] + '1'
                    codeword.append(new_data1 + new_data) 
                elif(word_size != len(data[i])):
                    print("Your length of dataword is not the same as word size")
            print("Codeword: ", codeword)  
    # Type of parity that user want to use
    elif(parity_type == 2):
        print("Your parity type is one-dimensional-odd")
        if(word_size < 5): 
            print("Your word size should equal or more than 5")
        else:
            raw_data = list(map(str, dataword.strip().split()))[:array_size] 
            print("Input Dataword - ", raw_data)
            # Separate dataword
            data = list(map(str, dataword.strip().split()))[:array_size] 
            for i in range(0, len(data)):
                if(len(data[i]) < word_size):
                    fill = data[i].zfill(word_size)
                    data[i] = fill 
            # Input
            print("Input Dataword - ", data)
            print("Word size: ", word_size)
            print("Array size: ", array_size)
            for i in range(0,array_size):
                count_1 = data[i].count(one)
                new_data = ""
                new_data1 = ""
                if(word_size == len(data[i])):
                    if(count_1 % 2 == 0):
                        # Put 1 into the dataword
                        new_data = data[i] + '1'
                    if(count_1 % 2  == 1):
                        # Put 0 into the dataword
                        new_data1 = data[i] + '0'
                    codeword.append(new_data1 + new_data) 
                elif(word_size != len(data[i])):
                    print("Your length of dataword is not the same as word size")
            print("Codeword: ", codeword)    
    # Type of parity that user want to use
    elif(parity_type == 3):
        print("Your parity type is two-dimensional-even")
        if(word_size < 5): 
            print("Your word size should equal or more than 5")
        else:
            raw_data = list(map(str, dataword.strip().split()))[:array_size] 
            print("Input Dataword - ", raw_data)
            # Separate dataword
            data = list(map(str, dataword.strip().split()))[:array_size] 
            for i in range(0, len(data)):
                if(len(data[i]) < word_size):
                    fill = data[i].zfill(word_size)
                    data[i] = fill 
            # Input
            print("Dataword - ", data)
            print("Word size: ", word_size)
            print("Array size: ", array_size)
            c=0
            arr = []
            x = []
            for r in range(0, len(data)):
                x = [int(b) for b in str(data[c])]
                arr.append(x)
                c+=1
            A = np.array(arr) 
            # Count one for rows
            count_one_r = 0
            # Count one for columns
            count_one_c = 0
            b = []
            new_arr = []
            for l in range(0, array_size): # Rows
                for m in range(0, word_size): # Columns
                    # Columns
                    if A[l,m] == 1: 
                        count_one_r += 1
                if(count_one_r % 2 == 0):
                    new_arr = arr[l] + [0]
                    l+=1
                if(count_one_r % 2 == 1):
                    new_arr = arr[l] + [1]
                # Make into string
                q = ''.join([str(item) for item in new_arr])
                # Count zero and one for columns
                count_one_r = 0
                b.append(new_arr) 
                codeword.append(q)  
            B = np.array(b) # Make into array to compute columns
            store_1 = []
            store_0 = []
            col_6 = []
            for j in range(0, word_size+1): # Rows
                for k in range(0, array_size): # Columns
                    # Columns
                    if B[k,j] == 1: 
                        count_one_c += 1
                if(count_one_c % 2 == 0):
                    store_0.append(0)
                if(count_one_c % 2 == 1):
                    store_0.append(1)
                # Count zero and one for columns
                count_one_c = 0
            col_6 = store_1 + store_0
            # Make into string
            p = ''.join([str(item) for item in col_6])
            codeword.append(p)
            print("Codeword: ", codeword) 
    # Type of parity that user want to use
    elif(parity_type == 4):
        print("Your parity type is two-dimensional-odd")
        if(word_size < 5): 
            print("Your word size should equal or more than 5")
        else:
            raw_data = list(map(str, dataword.strip().split()))[:array_size] 
            print("Input Dataword - ", raw_data)
            # Separate dataword
            data = list(map(str, dataword.strip().split()))[:array_size]
            for i in range(0, len(data)):
                if(len(data[i]) < word_size):
                    fill = data[i].zfill(word_size)
                    data[i] = fill  
            # Input
            print("Dataword - ", data)
            print("Word size: ", word_size)
            print("Array size: ", array_size)
            c=0
            arr = []
            x = []
            for r in range(0, len(data)):
                x = [int(b) for b in str(data[c])]
                arr.append(x)
                c+=1
            A = np.array(arr)
            # Count one for rows
            count_one_r = 0
            # Count one for columns
            count_one_c = 0
            b = []
            new_arr = []
            s = ""
            for l in range(0, array_size): # Rows
                for m in range(0, word_size): # Columns
                    # Columns
                    if A[l,m] == 1: 
                        count_one_r += 1
                if(count_one_r % 2 == 0):
                    new_arr = arr[l] + [1]
                    l+=1
                if(count_one_r % 2 == 1):
                    new_arr = arr[l] + [0]
                # Make into string
                q = ''.join([str(item) for item in new_arr])
                # Count zero and one for columns
                count_one_r = 0
                b.append(new_arr) 
                codeword.append(q)  
            B = np.array(b) # Make into array to compute columns
            store_1 = []
            store_0 = []
            col_6 = []
            for j in range(0, word_size+1): # Rows
                for k in range(0, array_size): # Columns
                    # Columns
                    if B[k,j] == 1: 
                        count_one_c += 1
                if(count_one_c % 2 == 0):
                    store_0.append(1)
                if(count_one_c % 2 == 1):
                    store_0.append(0)
                # Count zero and one for columns
                count_one_c = 0
            col_6 = store_1 + store_0
            # Make into string
            p = ''.join([str(item) for item in col_6])
            codeword.append(p)
            print("Codeword: ", codeword)  
    return codeword

def parity_check(codeword, parity_type):
    # PASS=1 or FAIL=0 
    # 1 Dimensional even
    if(parity_type == 1): # Type of parity that user want to use
        for i in range(len(codeword)):
            if codeword[i].count(one) % 2 == 1:
                print("FAIL")
                return 0
            elif codeword[i].count(one) % 2 == 0:
                print("PASS")
                return 1
    # 1 Dimensional odd
    if(parity_type == 2): # Type of parity that user want to use
        for i in range(len(codeword)):
            if codeword[i].count(one) % 2 == 1:
                print("PASS")
                return 1
            elif codeword[i].count(one) % 2 == 0:
                print("FAIL")
                return 0
    # 2 Dimensional even
    if(parity_type == 3): # Type of parity that user want to use
        c=0
        arr = []
        x = []
        for r in range(0, len(codeword)):
            x = [int(b) for b in str(codeword[c])]
            arr.append(x)
            c+=1
        A = np.array(arr)
        count_one_c = 0
        count_one_r = 0
        for i in range(0, len(codeword)+1): # Rows
            for j in range(0, len(codeword)): # Columns
                if A[j,i] == 1: 
                        count_one_c += 1
                if count_one_c % 2 == 0:
                    print("PASS")
                    return 1
                elif count_one_c % 2 == 1:
                    print("FAIL")
                    return 0
        for i in range(0, len(codeword)+1): # Rows
            for j in range(0, len(codeword)): # Columns
                if A[i,j] == 1: 
                    count_one_r += 1
                if count_one_r % 2 == 0:
                    print("PASS")
                    return 1
                elif count_one_r % 2 == 1:
                    print("FAIL")
                    return 0
    # 2 Dimensional odd
    if(parity_type == 4): # Type of parity that user want to use
        c=0
        arr = []
        x = []
        for r in range(0, len(codeword)):
            x = [int(b) for b in str(codeword[c])]
            arr.append(x)
            c+=1
        A = np.array(arr)
        count_one_c = 0
        count_one_r = 0
        for i in range(0, len(codeword)+1): # Rows
            for j in range(0, len(codeword)): # Columns
                if A[j,i] == 1: 
                        count_one_c += 1
                if count_one_c % 2 == 0:
                    print("FAIL")
                    return 0
                elif count_one_c % 2 == 1:
                    print("PASS")
                    return 1
        for i in range(0, len(codeword)+1): # Rows
            for j in range(0, len(codeword)): # Columns
                if A[i,j] == 1: 
                    count_one_r += 1
                if count_one_r % 2 == 0:
                    print("FAIL")
                    return 0
                elif count_one_r % 2 == 1:
                    print("PASS")
                    return 1


################### MAIN ###################
# Parity bit (Generator)
# dataword = input('Input Dataword: ')
# word_size = int(input('Input Word Size: '))
# parity_typeG = int(input('Input Parity Type: '))
# array_sizeG = int(input('Input Array Size: '))
# codeword = parity_gen(dataword, word_size, parity_typeG, array_sizeG)

# Parity bit (Checker)
# codeword = input('Input Codeword: ')
# parity_typeC = int(input('Input Parity Type: '))
# array_sizeC = int(input('Input Array Size: '))
# validity = parity_check(codeword, parity_typeC, array_sizeC)
#############################################

# Test Case (Generator)
# Input Dataword: 101101 110010 100000 001111 111111
# Input Word Size: 6
# Input Parity Type: 1
# Input Array Size: 5

# Test case (Checker)
# Input Codeword: 10110101100101100000100111101111110
# Input Parity Type: 1
# Input Array Size: 5