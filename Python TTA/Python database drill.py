import sqlite3

peopleValues = (

 ('Jean-Baptiste', 'Human', 122),

 ('Korben Dallas', 'Human', 100),

 ("Ak'not", 'Mangalore', -5)

 )

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()

c.execute("DROP TABLE IF EXISTS Roster")

c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, Iq INT)")
 
c.executemany("INSERT INTO Roster VALUES(?, ?, ?)",peopleValues)

c.execute("SELECT Name, Species, Iq FROM Roster")

#print peopleValues

c.execute("SELECT Name, Iq FROM Roster WHERE Species = 'Human'")
for row in c.fetchall():
    print row
