import sqlite3
from collections import defaultdict

conn = sqlite3.connect('ipl.db')
c = conn.cursor()

player_runs = c.execute('''SELECT PLAYER.player_id, PLAYER.player_name, BALL_BY_BALL.runs_scored
						   FROM PLAYER
						   INNER JOIN BALL_BY_BALL ON PLAYER.player_id=BALL_BY_BALL.striker''')

player_dict = defaultdict(lambda: ['', 0, 0, 0.0])	# [name, balls_faced, num_sixes, fraction_of_sixes]

for player in player_runs:
	player_dict[player[0]][0] = player[1]
	player_dict[player[0]][1] += 1
	if player[2] == 6:
		player_dict[player[0]][2] += 1

for k, v in player_dict.items():
	player_dict[k][3] = (1.0*v[2])/v[1]

sorted_list = [(a, b, d, c, e) for a, [b, c, d, e] in sorted(player_dict.items(), key=lambda item: item[1][3], reverse=True)]

for t, i in zip(sorted_list, range(20)):
	print("%d,%s,%d,%d,%f" % (t[0], t[1], t[2], t[3], t[4]))

conn.close()