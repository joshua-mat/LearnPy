# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number
# of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a
# maximum loop to find the most prolific committer.
import email
#open file
emailCount = dict()
fname = "mbox-short.txt"
#catch invalid file names
try:
    fh = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()
#loop through lines in files
for line in fh:
    #filter out lines starting ith From
    if line.startswith("From "):
        #Split "from" line and capture email into variable
        num = line[line.find('@')+1:line.isspace()]
        print(num)
        email = line.split()[1]
        #add emails to dictionary and add count for every occurrence using idiom
        emailCount[email] = emailCount.get(email, 0) + 1

l_email_value, l_email_key = None, None
# make dictionary into tuple and loop with key-value
for key, value in emailCount.items():
    # search for largest key-value and assign to vars
    if l_email_value is None or value > l_email_value:
        l_email_value = value
        l_email_key = key
        # print("largestCount",l_email_value)
print(l_email_key, l_email_value)



