# Hamming code 
import math

# Binary to decimal for Checker
def bi_to_dec(bi):
    count = len(bi) - 1
    list = []

    for i in range(len(bi)):
        list.append(int(bi[count]) * math.pow(2,i))
        count -= 1    
    # Total summation
    dec = sum(list)
    return -1 if int(dec)==0 else int(dec)

# Find parity bit of dataword for both
def find_P(data, act):
    p = 0 # Parity bit
    if act == 1:
        # Generator
        while math.pow(2, p) < p + len(data) + 1:
            p += 1
    elif act == 2:
        # Checker
        while math.pow(2, p) < len(data):
            p += 1        
    return p

# Arrange position for Generator
def arrange(data, p):
    k = len(data)     # Data length
    n = k + p         # Total length
    list = []         # New list position
    data = data[::-1] # Reverse dataword
    count_p = 0       # Count amount of parity bit
    count = 0        
    for i in range (0, n):
        if i == math.pow(2, count_p) - 1:
            list.append(0)
            count_p += 1
        else:
            list.append(int(data[count]))                 
            count += 1
    return list

# Solve hamming code for both
def solve(list, position, n, act):
    count = 0 # Count number 1 in list
    i = position - 1
    while i < n:
        for j in range (i, i + position):
            # Generator
            if j != position-1 and j < n and act == 1: 
                if list[j] == 1: 
                    count += 1
            # Checker
            if j < n and act == 2:
                if list[j] == 1: 
                    count += 1 
                      
        i = i + position + position # To skip to the next position
    if count % 2 == 0:
        return 0 #Even parity
    elif count % 2 == 1:
        return 1 #Odd parity

# Hamming code (Generator)
def Hamming_gen(dataword):
    p = find_P(dataword, 1)    #Function find number of parity bit
    n = len(dataword) + p      #Total number of codeword
    list = arrange(dataword,p) #Function check position
    
    for i in range (0, p):
       position = int(math.pow(2, i))
       temp = solve(list, position, n, 1)
       list[position-1] = temp

    # Reverse list   
    list.reverse()  
    # Change list to string
    listToStr = ' '.join(map(str, list))  
    return listToStr

# Hamming Code (Checker)
def Hamming_check(codeword):
    p = find_P(codeword, 2)    # Function find number of parity bit
    n = len(codeword)          # Total number of codeword
    list = []
    err = []                   # Error position
    # Change string to list
    for i in range (0, n):
        list.append(int(codeword[i]))

    # Reverse list   
    list.reverse()

    for i in range (0, p):
       position = int(math.pow(2, i))
       temp = solve(list, position, n, 2)
       err.append(temp)     

    # Reverse list   
    err.reverse()
    # Convert binary to decimal
    pos = bi_to_dec(err)
    return pos

################### MAIN ###################
# Hamming Code (Generator)
# dataword = input('Input Dataword: ') 
# codeword = Hamming_gen(dataword) 
# print("Codeword: " + codeword)

# Hamming Code (Checker)
# codeword = input('Input Codeword: ')
# error_pos = Hamming_check(codeword)
# print("Error at position:" , error_pos)
#############################################

# References
# https://www.geeksforgeeks.org/hamming-code-implementation-in-c-cpp/
# https://www.geeksforgeeks.org/hamming-code-implementation-in-python/#:~:text=Hamming%20code%20is%20a%20set,Hamming%20for%20error%20correction. 