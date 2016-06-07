import sqlite3

conn= sqlite3.connect('simpsons.db')

conn.execute("DELETE from SIMPSON_INFO where ID=3")

conn.commit()

changes = conn.total_changes
print "Number of changes: " ,changes

cursor = conn.execute("SELECT * from SIMPSON_INFO")

rows = cursor.fetchall()
print rows
