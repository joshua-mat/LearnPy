fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()
count = 0
for line in fh:
    if line.startswith("From "):
        email = line.split()[1]
        count += 1
        print(email)
print("There were", count, "lines in the file with From as the first word")
