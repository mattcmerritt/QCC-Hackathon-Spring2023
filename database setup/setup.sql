CREATE DATABASE schedules;
USE schedules;

-- UserSchedules
-- UserName		StartTime	EndTime		AvailabilityValue
-- varchar		time		time		int

CREATE TABLE UserSchedules (
	UserName			varchar(50)		PRIMARY KEY,
    StartTime			datetime,
    EndTime				datetime,
    AvailabilityValue	int
);

SELECT * FROM UserSchedules;

INSERT INTO UserSchedules (UserName, StartTime, EndTime, AvailabilityValue) VALUES ('Example', '2023-01-01', '2023-01-02', 0);