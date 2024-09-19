# a = range(1, 10)
# print(list(a))

# for numbers in range(11):
#     if numbers == 5:
#         continue
#     print(numbers)
    

# else:
#     print('Numbers are finished')

# To print prime numbers 
# while True:
#     num = int(input('Enter any number >>> '))
#     reversed_num = int(str(num)[::-2])
#     print(reversed_num)
 
# Fibonacci Series

# # Fibonacci Series
# N = int(input("Enter the number of terms: "))

# # First two terms
# a, b = 0, 1

# # Print the first N terms
# for _ in range(N):
#     print(a, end=" ")
#     a, b = b, a + b  # Update to the next Fibonacci number
# num  = '123'
# print(digits for digits in num)
# Sum = sum(int(digits) for digits in num)
# print(Sum)

number = '12390'
l =[]
for num in number:
    
    l.append(int(num))
print(sum(l))
