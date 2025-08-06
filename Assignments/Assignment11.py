import re

fn = input("Enter file name:")
try:
    fh = open(fn)
except:
    print("File does not exist")
    quit()
lst = list()
l_sum = 0

for line in fh :
    y = re.findall(r'\d+', line)
    if len(y) > 0:
        int_list = [int(s) for s in y]
        lst.append(int_list)

for l in lst :
    l_sum = l_sum + sum(l)
print(l_sum)
