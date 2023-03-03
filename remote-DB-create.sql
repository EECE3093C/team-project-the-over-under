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
    moneyline SERIAL NOT NULL, -- moneylines have no natural key so we default to auto-generated integers
    odds SMALLINT NOT NULL,
    contestant VARCHAR(30) NOT NULL,
    sportsbook VARCHAR(30) NOT NULL,
    PRIMARY KEY (moneyline),
    FOREIGN KEY (contestant) REFERENCES contestants(contestant),
    FOREIGN KEY (sportsbook) REFERENCES sportsbooks(sportsbook)
);