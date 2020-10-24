import sqlite3

conn = sqlite3.connect('ipl.db')
c = conn.cursor()

matches_runs = c.execute('''SELECT MATCH.venue_name, SUM(BALL_BY_BALL.runs_scored+BALL_BY_BALL.extra_runs), COUNT(DISTINCT MATCH.match_id)
							FROM MATCH
							INNER JOIN BALL_BY_BALL ON MATCH.match_id=BALL_BY_BALL.match_id
							GROUP BY MATCH.venue_name''')

final = [[x, y*1.0/z] for x, y, z in matches_runs]
final = sorted(final, key = lambda x : (-x[1], x[0]))
for stadium in final:
	print("{},{}".format(*stadium))

conn.close()