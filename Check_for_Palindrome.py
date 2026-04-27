list1 = []

list1.append(input("Enter the first element: "))
list1.append(input("Enter the second element: "))
list1.append(input("Enter the third element: "))

print(f"List 1: {list1}")

P = list1.copy()
P.reverse()
if P == list1:
    print("The list is Palindrome")
else:    print("The list is not Palindrome")