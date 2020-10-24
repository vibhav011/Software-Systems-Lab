import sqlite3

conn = sqlite3.connect('ipl.db')
c = conn.cursor()

player_runs = c.execute('''SELECT PLAYER.player_id, PLAYER.player_name, SUM(BALL_BY_BALL.runs_scored)
						   FROM PLAYER
						   INNER JOIN BALL_BY_BALL ON PLAYER.player_id=BALL_BY_BALL.striker
						   GROUP BY BALL_BY_BALL.striker''')

sorted_list = [(a, b, c) for a, b, c in sorted(player_runs.fetchall(), key=lambda x: (-x[2], x[1]))]

for t in sorted_list[:20]:
	print("%d,%s,%d" % (t[0], t[1], t[2]))

conn.close()