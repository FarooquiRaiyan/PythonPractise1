# . WAP to find Second largest element in an array = [12, 35, 1, 10, 34, 1, 35], without sorting,
# without using any built-in methods and without deleting duplicate elements. What will be the
# time complexity?


nums = [0,1,4,5,6, 9, 11, 99]
def second_largest(nums):
    largest = 0
    second_largest = 0
    for i in nums:
        if i > largest :
            second_largest = largest 
            largest = i
    return second_largest

print("second largest ",second_largest(nums))


# . WAP to reverse an integer without converting it to a string, without using any built-in methods. 

nums2 = 12345
def reverese_num(nums2):
   rem = 0
   n = 0
   temp=0
   while nums2 != 0: 
       print("remender is before ", rem, "nums2 is before ", nums2) 
       rem = nums2%10
       nums2 = nums2//10 
       temp = temp * 10 + rem
       print("remender is after ", rem, "nums2 is after ", nums2)
   return temp

print(reverese_num(nums2))  



# Swap Values without using any variable a=10, b=12.
def swp(a,b):
    a = a + b
    b = a-b 
    a = a- b
    print("a is ", a)
    print("b is ", b)
    return a,b

a = 10
b = 12
print(swp(a,b))



# Logic for anagram program with its time complexity. (for large strings).    need to chek viodeo
lists1 = ["tea", "ate", "bag", "gab", "gpa", "eat"]
lists2 = []
for i in lists1:
    for j in lists1:
        if sorted(i) == sorted(j) and i!=j:
            lists2.append(i)
            

print("anagram pairs are ", lists2)


# . Find the reverse of the string.

def reverse_string(name):
    rev = ""
    for i in name:
        rev = i + rev
    return rev

name = "hello world"
print(reverse_string(name))



# WAP to find missing elements from the array?

nums3 = [1,2,3,4,6,7,8,9]
missing = []
def missing_array(nums3):
    for i in range(1, len(nums3)+1):
        if i not in nums3:
            missing.append(i)
    return missing
print("missing elements are ", missing_array(nums3))



# WAP to find the given string is Palindrome or not check video for this question

def palindrome(str1):
    rev= ""
    for i in str1:
        rev = i + rev
    
    print("reverse is ", rev)
    if str1 == rev :
        print("this is palindrome", str1)
    else:
        print("this is not paindrome", str1)
        

palindrome("naga")



# 8. WAP to print Fibonacci series with recursion.
def fibonacci_1(nums3):
    if nums3 <= 1:
        return nums3
    else:
        return fibonacci_1(nums3-1) + fibonacci_1(nums3-2)
    
print("fibonacci of numbers is  ", fibonacci_1(4))



# 9. WAP to print Fibonacci series without recursion.
def fibonacci_2(n):

    a = 0
    b = 1

    for i in range(n):

        print(a, end=" ")

        temp = a + b
        a = b
        b = temp

print(fibonacci_2(10))




# 11. Code to find even numbers in a list
evens=[]
def find_evn(nums4):
    for i in nums4:
        if i%2==0:
            evens.append(i)
    return evens

print("evens are ", find_evn([1,2,3,4,5]))      



# 12. Find prime numbers from 1 ....n   not done need to check youtube 

def find_prime(nums6):
    primes = []
    for i in range(2,nums6):
        is_prime = True
        for j in range(2, i):
            if i%j == 0:
                is_prime = False
                break
        if is_prime :
            primes.append(i)
        
    return primes

print("primes numebsre are ", find_prime(8))



# WAP for getting a square root of a given number.

# def find_quare_root(nums6):
    
  
  
  
#   14. WAP with 2 different logic, to find all duplicate numbers in an array.


def find_duplicate(nums7):
    duplicates = []
    for i in nums7:
        if nums7.count(i) > 1 and i not in duplicates:
            duplicates.append(i)
    return duplicates

print("duplicates are ", find_duplicate([1,2,3,4,5,2,3,6]))


def find_duplicate2(nums7):
    duplicates = []
    seen = set()
    for i in nums7:
        if i in seen and i not in duplicates:
            duplicates.append(i)
        else:
            seen.add(i)
    return duplicates

print("duplicates are ", find_duplicate2([1,2,3,4,5,2,3,6]))




# 17. Given an array of strings, group the anagrams together. You can return the answer in any
# order.
# Input: str = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"

def find_anagrams():
    pass



#18 find the frquency of each and evry character in a string and sort in descending order
# Input : Engineer 
# Output : e3n2g1i1r1


def find_fre_cha(str2):
    freq = {}
    for i in str2.lower():
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    
    result =""
    for key,value in freq.items():
        result = result + key + str(value)
    return result


print("Frquency andChacter ", find_fre_cha("Engineer"))
            
            
            
            
           
# count lower and upper chars

def count_lower_upper(str5):
    lower_count = 0
    uppercount = 0
    for i in str5:
        if i.islower():
            lower_count += 1
        elif i.isupper():
            uppercount += 1
        else:
            None

    return lower_count, uppercount


strname  = "Hello Enginner"
lower, upper = count_lower_upper(strname)
print("lower count ", lower)
print("upper count is ", upper)   
        
            
            


# 19 sum of squares of first n prime numbers 

def prime_number_squares(nos2):
    for i in range(2, ((nos2//2)+1)):
        if nos2 % i == 0:
            return None 
    return nos2* nos2
        


start = 1
end = 25
nos = end 
list3 = []
for i in range(1, nos+1):
    a = prime_number_squares(i)
    if a is not None :
        list3.append(a)
print("prime number witht the squares",list3)
        
        
        
# 4, 5, 6 , 7,8,9, 
# 11,12,13,6,7,8,9
# These two are linked list , Find point of common element ?
# Logc fior above problem 
# What will be complexity for it 
# Any better solution   


class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None
    

node1 = Node(15)
node2= Node(30)
node3 = Node(45)   
node1.next = node2
node2.next = node3 


head = node1

current = head 
while current : 
    print("cureen.data", current.value)
    current = current.next
print("None")
              
