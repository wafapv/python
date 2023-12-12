lst = [-1, 2, -3, 4, -5, 6]
positive_numbers = [num for num in lst if num > 0]
print("Positive ", positive_numbers)
N = 5
squares = [i ** 2 for i in range(1, N+1)]
print("Squares up to N ", squares)
word = 'Hello World'
vowels = [char for char in word if char.lower() in 'aeiou']
print("Vowels ", vowels)
word = 'Hello World'
ordinal_values = [ord(char) for char in word]
print("Ordinal values", ordinal_values)