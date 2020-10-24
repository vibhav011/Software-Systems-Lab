import sqlite3

conn = sqlite3.connect('ipl.db')
with conn:
    c = conn.cursor()

    c.execute("""CREATE TABLE TEAM(
        team_id INTEGER,
        team_name text,
        PRIMARY KEY (team_id)
    )

    """)

    c.execute("""CREATE TABLE PLAYER(
        player_id INTEGER,
        player_name text,
        dob TIMESTAMP,
        batting_hand text,
        bowling_skill text,
        country_name text,
        PRIMARY KEY (player_id)
    )

    """)

    c.execute("""CREATE TABLE MATCH(
        match_id INTEGER,
        season_year INTEGER,
        team1 INTEGER,
        team2 INTEGER,
        battedfirst INTEGER,
        battedsecond INTEGER,
        venue_name text,
        city_name text,
        country_name text,
        toss_winner INTEGER,
        match_winner INTEGER,
        toss_name text,
        win_type text,
        man_of_match INTEGER,
        win_margin INTEGER,
        PRIMARY KEY (match_id),
        FOREIGN KEY (team1) REFERENCES team (team_id),
        FOREIGN KEY (team2) REFERENCES team (team_id),
        FOREIGN KEY (battedfirst) REFERENCES team (team_id),
        FOREIGN KEY (battedsecond) REFERENCES team (team_id)
    )

    """)

    c.execute("""CREATE TABLE PLAYER_MATCH(
        playermatch_key INTEGER,
        match_id INTEGER,
        player_id INTEGER,
        batting_hand text,
        bowling_skill text,
        role_desc text,
        team_id INTEGER,
        PRIMARY KEY (playermatch_key),
        FOREIGN KEY (match_id) REFERENCES match (match_id),
        FOREIGN KEY (player_id) REFERENCES player (player_id),
        FOREIGN KEY (team_id) REFERENCES team (team_id)
    )

    """)

    c.execute("""CREATE TABLE BALL_BY_BALL(
        match_id INTEGER,
        innings_no INTEGER,
        over_id INTEGER,
        ball_id INTEGER,
        striker_batting_position INTEGER,
        runs_scored INTEGER,
        extra_runs INTEGER,
        out_type text,
        striker INTEGER,
        non_striker INTEGER,
        bowler INTEGER,
        PRIMARY KEY (match_id, innings_no, over_id, ball_id),
        FOREIGN KEY (striker) REFERENCES player (player_id),
        FOREIGN KEY (non_striker) REFERENCES player (player_id),
        FOREIGN KEY (bowler) REFERENCES player (player_id),
        FOREIGN KEY (match_id) REFERENCES match (match_id)
    )

    """)