import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS counts')

cur.execute('CREATE TABLE counts (org TEXT, count INTEGER)')

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox.txt"
fh = open(fname)

for line in fh:
    if not line.startswith("From "): continue
    pieces = line.split()
    email = pieces[1]
    org = email.split('@')[1]
    cur.execute('SELECT count FROM counts WHERE org = ?', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO counts VALUES(?, 1)', (org,))
    else:
        cur.execute('UPDATE counts SET count = count + 1 WHERE org = ?', (org,))
    conn.commit()

sqlstr = 'SELECT org, count FROM counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
cur.close()