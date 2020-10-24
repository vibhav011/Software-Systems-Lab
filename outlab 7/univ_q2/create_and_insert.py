import sqlite3

conn = sqlite3.connect("univ.db")
c = conn.cursor()

with open("University Schema", 'r') as f:
    s = f.read()
    commands = s.split(';')
    for command in commands:
        try:
            c.executescript(command)
        except:
            pass
    conn.commit()

with open("smallRelationsInsertFile.sql", 'r') as f:
    s = f.read()
    commands = s.split(';')
    for command in commands:
        try:
            c.executescript(command)
        except:
            pass
    conn.commit()