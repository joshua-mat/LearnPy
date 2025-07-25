# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and
# put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None

while True:
    num = input("Enter number:")
    try:
        if num == 'done' :
            break
        n = int(num)
        if smallest is None or n < smallest:
            smallest = n
        if largest is None or n > largest:
            largest = n
    except:
        print("Invalid input")
        # continue

print("Largest number:", largest)
print("Smallest number:", smallest)


