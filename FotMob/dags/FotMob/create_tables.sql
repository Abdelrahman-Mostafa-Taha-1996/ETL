-- create teams table sql
CREATE TABLE IF NOT EXISTS fotmob.teams (
    team_id INT PRIMARY KEY,
    team_name VARCHAR(100),
    short_name VARCHAR(100)
);

-- create matches table sql 
CREATE TABLE IF NOT EXISTS fotmob.matches (
    match_id SERIAL PRIMARY KEY,
    season VARCHAR(10),
    round VARCHAR(5) NOT NULL,
    home_team_id INT REFERENCES fotmob.teams(team_id),
    away_team_id INT REFERENCES fotmob.teams(team_id),
    score VARCHAR(10),
    time TIMESTAMP
);

-- create standings table sql
CREATE TABLE IF NOT EXISTS fotmob.standings (
    standing_id SERIAL PRIMARY KEY,
    season VARCHAR(10) NOT NULL,
    team_id INT REFERENCES fotmob.teams(team_id),
    rank INT NOT NULL,
    played INT NOT NULL,
    wins INT NOT NULL,
    draws INT NOT NULL,
    losses INT NOT NULL,
    points INT NOT NULL,
    scoreStr VARCHAR(10),
    goalConDiff INT
);