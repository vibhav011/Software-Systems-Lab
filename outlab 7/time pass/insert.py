import sqlite3, csv

conn = sqlite3.connect('ipl.db')
with conn:
    c = conn.cursor()

    with open ('team.csv', 'r') as f:
        next(f)
        rows = csv.reader(f)
        c.executemany("INSERT INTO TEAM VALUES (?, ?)", rows)

    with open ('match.csv', 'r') as f:
        next(f)
        rows = csv.reader(f)
        c.executemany("INSERT INTO MATCH VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", rows)

    with open ('player.csv', 'r') as f:
        next(f)
        rows = csv.reader(f)
        c.executemany("INSERT INTO PLAYER VALUES (?, ?, ?, ?, ?, ?)", rows)

    with open ('player_match.csv', 'r') as f:
        next(f)
        rows = csv.reader(f)
        c.executemany("INSERT INTO PLAYER_MATCH VALUES (?, ?, ?, ?, ?, ?, ?)", rows)

    with open ('ball_by_ball.csv', 'r') as f:
        next(f)
        rows = csv.reader(f)
        c.executemany("INSERT INTO BALL_BY_BALL VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", rows)