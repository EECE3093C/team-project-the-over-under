CREATE DATABASE mainline;

-- Create tables per data model as of 2/23.
CREATE TABLE competitions (
	competition VARCHAR(30) NOT NULL, -- 30 characters seems to be an upper bound for name length
    PRIMARY KEY (competition)
);
CREATE TABLE contestants (
	contestant VARCHAR(30) NOT NULL,
    form VARCHAR(5) NULL, -- we store recent results as a 5-character string like 'WLDWW'
    opponent VARCHAR(30) NULL, -- form and next opponent are nullable because they aren't available in the offseason
    competition VARCHAR(30) NOT NULL,
    PRIMARY KEY (contestant),
    FOREIGN KEY (competition) REFERENCES competitions(competition)
);
CREATE TABLE sportsbooks (
	sportsbook VARCHAR(30) NOT NULL,
    url VARCHAR(2048) NOT NULL, -- the address bar can only contain 2048 characters
    PRIMARY KEY (sportsbook)
);
CREATE TABLE moneylines (
	moneyline INT NOT NULL AUTO_INCREMENT, -- moneylines have no natural key so we default to auto-generated integers
    odds SMALLINT NOT NULL,
	contestant VARCHAR(30) NOT NULL,
    sportsbook VARCHAR(30) NOT NULL,
    PRIMARY KEY (moneyline),
    FOREIGN KEY (contestant) REFERENCES contestants(contestant),
    FOREIGN KEY (sportsbook) REFERENCES sportsbooks(sportsbook)
);

-- Populate tables with first set of "permanent" data.
INSERT INTO competitions
VALUES ('Premier League');
INSERT INTO contestants (contestant, competition)
VALUES
('Arsenal', 'Premier League'),
('Man City', 'Premier League'),
('Man United', 'Premier League'),
('Tottenham', 'Premier League'),
('Newcastle', 'Premier League'),
('Fulham', 'Premier League'),
('Brighton', 'Premier League'),
('Liverpool', 'Premier League'),
('Brentford', 'Premier League'),
('Chelsea', 'Premier League'),
('Aston Villa', 'Premier League'),
('Crystal Palace', 'Premier League'),
('Nottm Forest', 'Premier League'),
('Leicester City', 'Premier League'),
('Wolves', 'Premier League'),
('Everton', 'Premier League'),
('Bournemouth', 'Premier League'),
('West Ham', 'Premier League'),
('Leeds United', 'Premier League'),
('Southampton', 'Premier League');
INSERT INTO sportsbooks
VALUES
('DraftKings', 'https://sportsbook.draftkings.com/sportsbook?wpsrc=Organic%20Search&wpaffn=Google&wpkw=https%3A%2F%2Fwww.draftkings.com%2F'),
('FanDuel', 'https://www.fanduel.com/'),
('bet365', 'https://www.oh.bet365.com/?_h=gNkRA335CIkgWRZEjMPltQ%3D%3D#/HO/'),
('PointsBet', 'https://oh.pointsbet.com/'),
('BetMGM', 'https://sports.oh.betmgm.com/en/sports');
