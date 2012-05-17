CREATE TABLE IF NOT EXISTS racers
(  
    name                TEXT,
    id                  INTEGER PRIMARY KEY
);
CREATE TABLE IF NOT EXISTS cars
(
	id					INTEGER PRIMARY KEY,
	name				UNIQUE TEXT,
	owner				INTEGER,
	xclass				TEXT
);
CREATE TABLE IF NOT EXISTS races_racers
(
	racer_id			INTEGER,
	race_id				INTEGER
);
CREATE TABLE IF NOT EXISTS races
(
	id					INTEGER PRIMARY KEY,
	rclass				TEXT,
	start_time			INTEGER
);
CREATE TABLE IF NOT EXISTS heats_racers
(
	racer_id			INTEGER,
	heat_id				INTEGER,
	race_id				INTEGER,
)

CREATE TABLE IF NOT EXISTS heats
(
	id					INTEGER PRIMARY KEY,
	race_id				INTEGER
);
CREATE TABLE IF NOT EXISTS laps
(
	id					INTEGER PRIMARY KEY,
	heat_id				INTEGER,
	racer_id			INTEGER,
	car_id				INTEGER
);