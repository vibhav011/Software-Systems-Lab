import sqlite3, csv

conn = sqlite3.connect('ipl.db')
with conn:
    c = conn.cursor()

    stad = {}
    data = c.execute("""SELECT venue_name, SUM(runs_scored), SUM(extra_runs) 
                FROM BALL_BY_BALL 
                INNER JOIN MATCH ON MATCH.match_id = BALL_BY_BALL.match_id 
                GROUP BY BALL_BY_BALL.match_id""")

    for match in data:
        venue = match[0]
        if venue not in stad:
            stad[venue] = [0, 0]
        stad[venue][0] += match[1] + match[2]
        stad[venue][1] += 1

    final = [(key, value[0]*1.0/value[1]) for key, value in stad.items()]
    final = sorted(final, key = lambda x : x[1], reverse = True)
    for pair in final:
        x = list(map(str, pair))
        print(','.join(x))