import sqlite3

conn = sqlite3.connect('ipl.db')
with conn:
    c = conn.cursor()
    data = c.execute("""
        SELECT PLAYER.player_id, PLAYER.player_name, SUM(runs_scored = 6), COUNT(*)
        FROM BALL_BY_BALL
        INNER JOIN PLAYER on PLAYER.player_id = BALL_BY_BALL.striker
        WHERE runs_scored != 'NULL'
        GROUP BY striker
    """)

    final = [[x, y, z, w, z*1.0/w] for x, y, z, w in data]
    final = sorted(final, key = lambda x : (-x[4], x[1]))
    for player in final:
        x = list(map(str, player))
        print(",".join(x))