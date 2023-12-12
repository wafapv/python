string = input("Enter the numbers separated by space: ")

original_list = [int(x) for x in string.split()] 
new_list = [x for x in original_list if x % 2 != 0] 
print("New List:", new_list)