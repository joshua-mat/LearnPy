# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each
# of the messages. You can pull the hour out from the 'From ' line by finding the time
# and then splitting the string a second time using a colon. From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
hCount = dict()
fname  = input('Enter file name: ')
try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
for line in fh:
    if line.startswith('From'):
        words = line.split()
        if len(words) > 2:
            time = words[5]
            hour = time.split(":")[0]
            hCount[hour] = hCount.get(hour, 0) + 1
for k,v in sorted(hCount.items()):
    print(k,v)