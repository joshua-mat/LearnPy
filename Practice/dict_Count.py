print("Enter a line of text:")
line = input('')
words = line.split()
print('Words', words)
print('counting...')
counts = dict()
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts:', counts)
print('Keys', counts.keys())