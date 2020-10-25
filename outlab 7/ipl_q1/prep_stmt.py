import sys, sqlite3

table_names = ['TEAM', 'PLAYER', 'MATCH', 'PLAYER_MATCH', 'BALL_BY_BALL']

conn = sqlite3.connect('ipl.db')
with conn:
	c = conn.cursor()

	query = "INSERT INTO " + table_names[int(sys.argv[1])-1] + " VALUES (?" + (", ?"*(len(sys.argv)-3)) + ")";
	vals = tuple(sys.argv[2:])
	c.execute(query, vals)