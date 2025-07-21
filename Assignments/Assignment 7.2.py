# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count, tot = 0 , 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        num = line[line.find(':')+1:]
        n = num.rstrip()
        tot = tot + float(num)
        avg = tot / count
print('Average spam confidence:', avg)

