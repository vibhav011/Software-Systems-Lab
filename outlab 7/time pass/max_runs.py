import sqlite3

conn = sqlite3.connect('ipl.db')
with conn:
    c = conn.cursor()
    data = c.execute("""
        SELECT striker, PLAYER.player_name, SUM(runs_scored)
        FROM BALL_BY_BALL
        INNER JOIN PLAYER ON PLAYER.player_id = BALL_BY_BALL.striker
        GROUP BY striker
    """)

    final = [player for player in data]
    final = sorted(final, key = lambda x: (-x[2], x[1]))
    for x in final[:20]:
        y = list(map(str, x))
        print(",".join(y))