# 1. Print sum of first n numbers
# E.g. n=5, output=15 (1+2+3+4+5=15)


def print_first_n(n):
    sum = 0
    nums = []
    for i in range(1, n+1):
        sum = sum + i 
        nums.append(i)
    return sum , nums

total_sum, numbers = print_first_n(5)
print("sum of first n numbers is ", total_sum)
for i in numbers:
    print(i , "+", end=" ")
print("= ", total_sum)
    
  
  
  
    
# Print list of onumber from 1 - n-1 dd and even 
def print_even_odd(n):
    even_no  = []
    odd_no = [] 
    for i in range(1, n+1):
        if i%2 == 0:
            even_no.append(i)
        else:
            odd_no.append(i)
    return even_no, odd_no

odds, evens = print_even_odd(10)
print("odds are ", odds)
print("evens are ", evens)



# Use while loops and print following pattern :
# n = 19 
# 1,2,3,4,5 *, *, *, *, *, 11,12, 13, 14, 15 , *, *, *, *


n = 10
block_size = 5

i = 1

while i <= n:

    block = (i - 1) // block_size
    print("block is ", block)
    # even block -> numbers
    if block % 2 == 0:
        print(i, end=" ")

    # odd block -> stars
    else:
        print("*", end=" ")

    i += 1  
    print()
    




# find factorial
def factorial(n):
    facto = 1
    if n == 1 or n ==0:
            return facto
    for i in range(2, n+1):
        facto = facto * i 
    return facto


print(factorial(4))




#  prime number or not 


#6  pattern 

def pattern_2 (n):
    for i in range(n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()
        
pattern_2(3)




# 7 pattern 

def pattern_3(n):
    for i in range(n+1):
        for j in range(1, i):
            print(j)
            
pattern_3(4)




# 8 generate dictionaty which stores count of appearance 
# input = "aabbccddd"
# output = {"a":2, "b":2,"c":2, "d":3}

def count_words(words):
    new_words = {}
    for i in words:
        if words.lower() and i not in new_words:
            new_words.add(i)
            counts = i.count() 
            new_words.append(i)





# find intersection of two lists 
list1 = [1,2,3,4,5]
list2 = [3,4,6]

inter_list = []
def find_inter(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                inter_list.append(i)
    return inter_list


print("print find interlist ", find_inter(list1, list2))
      




# palindrome word
def palindrome(str2):
    rev = ""
    for i in str2:
        rev = i + rev
    
    if rev == str2:
        print("plaindrome", str2)
    else:
        print("not palindrome",str2 )
    
    return rev

print("palindrome unction ", palindrome("HelleH"))




# fibonacci series return the sequence as well

def fibo(n):
    t1= 0
    t2=1
    temp = 0
    if n ==0 :
        return t1
    elif n == 1:
        return t2
    else:
        return fibo(n-1) + fibo(n-2)

print("fibo", fibo(4))







matrix = [[1,2,3],[4,5,6]]
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transpose = []
    for i in range(cols) :
        temp = []
        for j in range(rows):
            temp.append(matrix[j][i])
            print("temp is ", temp)
        transpose.append(temp)
    return transpose

print("transpose matrix", transpose_matrix(matrix))



#  write a code to achive belwo pattern 
# 54321
# DCBA
# 321
# BA
# 1


# # Valid paranthesis 
# Given a string s containing just the characters '(', '(', '{', '}', '[', ']', determine if the input sring is valid 
# An input tsirng is valid if :
#     open brakcet must be lcosed by same bracket
#     open bracket must be closed in correct order
#     ecery close bracket hass the open bracket of same type
    
# "exapple"
# s = "()[]{}"
# output = true

# s2 = "({])"
# output = False




def valid_para(parant):
    stack = []
    pairs = {
        ')':'(',
        '}':'{',
        ']':'['
    }
    
    
    for char in parant:
        if char in "({[":
            stack.append(char)
        else:
            
            if len(stack) == 0:
                return False 
            
            top = stack.pop()
            
            if pairs[char] != top:
                return False
    
    return len(stack) == 0

print("stacks data ", valid_para("{({[]}}"))







# Linekd List 

# binary search 
def binary_search_fun(nums2, target):
    low = 0
    high = len(nums2) - 1
    
    while low <= high :
        mid = (low + high) // 2
        
        if nums2[mid] == target :
            return mid
        elif nums2[mid] < target :
            low = mid + 1
        else:
            high = mid - 1
    return -1

print("binary search ", binary_search_fun([1,2,3,4], 3))


# prime or not


def is_prime(no):
    if (no ==1) or (no == 0):
        return False
    
    for i in range (2, ((no//2)+1)):
        if no%i == 0 :
            return False
    
    
    return no
    

ist = []
no = 20

for i in range(1, no + 1 ):
    nos = is_prime(i)
    ist.append(nos)
    
    
print("ist ", ist)
        
while False in ist:
    ist.remove(False)
    
print("list updated", ist)


