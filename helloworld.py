def swap(string1, string2):
    temp = string1
    string1 = string2
    string2 = temp
    print(string1 + " " + string2)

string1 = input("Enter 1st string: ")
string2 = input("Enter 2nd string: ")
swap(string1, string2)