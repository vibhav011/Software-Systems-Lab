import sqlite3
from collections import defaultdict, Counter

conn = sqlite3.connect('ipl.db')
c = conn.cursor()

matches_runs = c.execute('''SELECT MATCH.venue_name, SUM(BALL_BY_BALL.runs_scored), SUM(BALL_BY_BALL.extra_runs)
						   FROM MATCH
						   INNER JOIN BALL_BY_BALL ON MATCH.match_id=BALL_BY_BALL.match_id
						   GROUP BY MATCH.match_id''')

avg_runs = defaultdict(float)
cnt = Counter()

for match in matches_runs:
	avg_runs[match[0]] += match[1]
	cnt[match[0]] += 1

for k in avg_runs:
	avg_runs[k] /= cnt[k]

sorted_list = [(k, v) for k, v in sorted(avg_runs.items(), key=lambda item: item[1], reverse=True)]

for pair in sorted_list:
	print("%s,%f" % (pair[0], pair[1]))

conn.close()