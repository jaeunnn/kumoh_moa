CREATE TABLE bachelor (
    not_id VARCHAR PRIMARY KEY,
    not_title VARCHAR NOT NULL,
    not_date VARCHAR NOT NULL,
    not_url VARCHAR NOT NULL
);

CREATE TABLE event (
    evt_id VARCHAR PRIMARY KEY,
    evt_title VARCHAR NOT NULL,
    evt_date VARCHAR NOT NULL,
    evt_url VARCHAR NOT NULL
);

CREATE TABLE cheering (
    cheer_id SERIAL PRIMARY KEY,
    cheer_message VARCHAR NOT NULL
);
