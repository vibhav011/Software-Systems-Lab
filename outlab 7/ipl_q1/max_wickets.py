import sqlite3
from collections import defaultdict

conn = sqlite3.connect('ipl.db')
c = conn.cursor()

player_wickets = c.execute('''SELECT PLAYER.player_id, PLAYER.player_name, BALL_BY_BALL.out_type
						   FROM PLAYER
						   INNER JOIN BALL_BY_BALL ON PLAYER.player_id=BALL_BY_BALL.bowler''')


my_dict = defaultdict(lambda : 1)
my_dict['Not Applicable'] = 0;

player_dict = defaultdict(lambda : ['', 0])

for player in player_wickets:
	player_dict[player[0]][1] += my_dict[player[2]]
	player_dict[player[0]][0] = player[1]

sorted_list = [(a, b, c) for a, [b, c] in sorted(player_dict.items(), key=lambda item: item[1][1], reverse=True)]

for t, i in zip(sorted_list, range(20)):
	print("%d,%s,%d" % (t[0], t[1], t[2]))

conn.close()