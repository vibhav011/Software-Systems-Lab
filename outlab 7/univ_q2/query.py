import sqlite3, sys

conn = sqlite3.connect("univ.db")
c = conn.cursor()
with conn:

    f, num, tab, column, value = sys.argv
    if num == '0':
        try:
            s = "SELECT * FROM " + tab + " WHERE " + column +"= '" + value + "'"
            c.execute(s)
            for row in c.fetchall():
                row = list(map(str, row))
                print(",".join(row))
        except:
            pass

    else:
        try:
            s="SELECT * FROM " + tab + " WHERE " + column + "= ?"
            c.execute(s, (value,))
            for row in c.fetchall():
                row = list(map(str, row))
                print(",".join(row))
        except:
            pass