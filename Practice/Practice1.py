largest = None
smallest = None
lst = list()
while True:
    num = input("Enter number:")
    try:
        if num == 'done' :
            break
        n = int(num)
        lst.append(n)
    except:
        print("Invalid input")
        # continue
print(lst)
print("Largest number:", max(lst))
print("Smallest number:", min(lst))