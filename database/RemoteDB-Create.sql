-- Create tables per ERD as of 3/9.
CREATE TABLE competitions (
    competition VARCHAR(30) NOT NULL, -- 30 characters seems to be an upper bound for name length
    PRIMARY KEY (competition)
);
CREATE TABLE contestants (
    contestant VARCHAR(30) NOT NULL,
    form VARCHAR(5) NULL, -- we store recent results as a 5-character string like 'WLDWW'
    PRIMARY KEY (contestant)
);
CREATE TABLE sportsbooks (
    sportsbook VARCHAR(30) NOT NULL,
    url VARCHAR(2048) NOT NULL, -- the address bar can only contain 2048 characters
    PRIMARY KEY (sportsbook)
);
CREATE TABLE matchups (
    matchup SERIAL NOT NULL, -- matchups have no natural key so we default to auto-generated integers
    home VARCHAR(30) NULL, -- sometimes you can bet on matchups before the contestants are decided, like the Super Bowl
    away VARCHAR(30) NULL,
    competition VARCHAR(30) NOT NULL,
    PRIMARY KEY (matchup),
    FOREIGN KEY (home) REFERENCES contestants(contestant),
    FOREIGN KEY (away) REFERENCES contestants(contestant),
    FOREIGN KEY (competition) REFERENCES competitions(competition)
);
CREATE TABLE moneylines (
    moneyline SERIAL NOT NULL, -- moneylines have no natural key so we default to auto-generated integers
    odds SMALLINT NOT NULL,
    type CHAR(1) NOT NULL, -- type identifier H, A, D for home, away, draw
    matchup INT NOT NULL,
    sportsbook VARCHAR(30) NOT NULL,
    PRIMARY KEY (moneyline),
    FOREIGN KEY (matchup) REFERENCES matchups(matchup),
    FOREIGN KEY (sportsbook) REFERENCES sportsbooks(sportsbook)
);

-- Populate tables with first set of "permanent" data.
INSERT INTO competitions
VALUES
    ('Premier League');
INSERT INTO contestants(contestant)
VALUES
    ('Arsenal'),
    ('Man City'),
    ('Man United'),
    ('Tottenham'),
    ('Liverpool'),
    ('Newcastle'),
    ('Fulham'),
    ('Brighton'),
    ('Brentford'),
    ('Chelsea'),
    ('Aston Villa'),
    ('Crystal Palace'),
    ('Wolves'),
    ('Nottm Forest'),
    ('Leicester City'),
    ('West Ham'),
    ('Leeds United'),
    ('Everton'),
    ('Southampton'),
    ('Bournemouth');
INSERT INTO sportsbooks
VALUES
    ('FanDuel', 'https://www.fanduel.com/'),
    ('BetMGM', 'https://sports.oh.betmgm.com/en/sports'),
    ('DraftKings', 'https://www.draftkings.com/?wpsrc=Organic%20Search&wpaffn=Google&wpkw=https%3A%2F%2Fwww.draftkings.com%2F'),
    ('PointsBet', 'https://oh.pointsbet.com/'),
    ('Barstool', 'https://www.barstoolsportsbook.com/')