import sqlite3

conn = sqlite3.connect("ipl.db")

with conn:
	c = conn.cursor()
	team = {}
	data = c.execute("SELECT * FROM TEAM")
	for row in data:
		team[row[0]] = [row[1], 0, 0]
	c.execute("""CREATE TABLE POINTS_TABLE(
		team_id INTEGER,
		team_name text,
		points INTEGER,
		nrr REAL
	)""")

	data = c.execute("SELECT * FROM MATCH")

	for row in data:
		if row[12] != 'runs' and row[12] != 'wickets':
			team[row[2]][1] += 1
			team[row[3]][1] += 1
			continue
		elif row[10] == row[2]:
			team[row[2]][1] += 2
			if row[12] == 'runs':
				team[row[2]][2] += row[14]/20
				team[row[3]][2] -= row[14]/20
			else:
				team[row[2]][2] += row[14]/10
				team[row[3]][2] -= row[14]/10
		else:
			team[row[3]][1] += 2
			if row[12] == 'runs':
				team[row[3]][2] += row[14]/20
				team[row[2]][2] -= row[14]/20
			else:
				team[row[3]][2] += row[14]/10
				team[row[2]][2] -= row[14]/10

	final = [(key, value[0], value[1], value[2]) for key, value in team.items()]
	c.executemany("INSERT INTO POINTS_TABLE VALUES (?, ?, ?, ?)", final)

	data = c.execute("SELECT * FROM POINTS_TABLE")
	data = sorted(data, key = lambda x : (x[2], x[3]), reverse = True)
	for row in data:
		x = list(map(str, row))
		print(",".join(x))