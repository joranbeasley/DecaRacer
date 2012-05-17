CREATE TABLE IF NOT EXISTS racers
(  
    name                TEXT,
	seed				INTEGER,
	heightMap			TEXT,
    id                  INTEGER PRIMARY KEY,
	width				INTEGER,
	height				INTEGER,
	maxGray				INTEGER
);