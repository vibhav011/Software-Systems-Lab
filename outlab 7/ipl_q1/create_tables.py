import sqlite3

conn = sqlite3.connect('ipl.db')
c = conn.cursor()

c.execute('''CREATE TABLE TEAM
				(team_id integer PRIMARY KEY,
				 team_name text)''')

c.execute('''CREATE TABLE PLAYER 
				(player_id integer PRIMARY KEY,
				 player_name text,
				 dob timestamp,
				 batting_hand text,
				 bowling_skill text,
				 country_name text)''')

c.execute('''CREATE TABLE MATCH
				(match_id integer PRIMARY KEY,
				 season_year integer,
				 team1 integer,
				 team2 integer,
				 battedfirst integer,
				 battedsecond integer,
				 venue_name text,
				 city_name text,
				 country_name text,
				 toss_winner text,
				 match_winner integer,
				 toss_name text,
				 win_type text,
				 man_of_match integer,
				 win_margin integer,
				 FOREIGN KEY (team1) REFERENCES TEAM (team_id),
				 FOREIGN KEY (team2) REFERENCES TEAM (team_id),
				 FOREIGN KEY (battedfirst) REFERENCES TEAM (team_id),
				 FOREIGN KEY (battedsecond) REFERENCES TEAM (team_id))''')

c.execute('''CREATE TABLE PLAYER_MATCH
				(playermatch_key bigint PRIMARY KEY,
				 match_id integer,
				 player_id integer,
				 batting_hand text,
				 bowling_skill text,
				 role_desc text,
				 team_id integer,
				 FOREIGN KEY (match_id) REFERENCES MATCH (match_id),
				 FOREIGN KEY (player_id) REFERENCES PLAYER (player_id),
				 FOREIGN KEY (team_id) REFERENCES TEAM (team_id))''')

c.execute('''CREATE TABLE BALL_BY_BALL
				(match_id integer,
				 innings_no integer,
				 over_id integer,
				 ball_id integer,
				 striker_batting_position integer,
				 runs_scored integer,
				 extra_runs integer,
				 out_type text,
				 striker integer,
				 non_striker integer,
				 bowler integer,
				 PRIMARY KEY (match_id, innings_no, over_id, ball_id),
				 FOREIGN KEY (match_id) REFERENCES MATCH (match_id)
				 FOREIGN KEY (striker) REFERENCES PLAYER (player_id),
				 FOREIGN KEY (non_striker) REFERENCES PLAYER (player_id),
				 FOREIGN KEY (bowler) REFERENCES PLAYER (player_id))''')

conn.commit()
conn.close()