import sqlite3

conn = sqlite3.connect('ipl.db')
with conn:
    c = conn.cursor()
    data = c.execute("""
    
        SELECT bowler, PLAYER.player_name, COUNT(*)
        FROM BALL_BY_BALL
        INNER JOIN PLAYER ON PLAYER.player_id = BALL_BY_BALL.bowler
        WHERE out_type != 'Not Applicable'
        GROUP BY bowler
    """)

    final = [player for player in data]
    final = sorted(final, key = lambda x: (-x[2], x[1]))
    for x in final[:20]:
        print("{},{},{}".format(*x))