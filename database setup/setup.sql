CREATE DATABASE schedules;
USE schedules;

-- UserSchedules
-- UserName		StartTime	EndTime		AvailabilityValue
-- varchar		time		time		int

CREATE TABLE UserSchedules (
	UserName			varchar(50),
    StartTime			datetime,
    EndTime				datetime,
    AvailabilityValue	int
);

SELECT * FROM UserSchedules;

TRUNCATE UserSchedules;

-- INSERT INTO UserSchedules (UserName, StartTime, EndTime, AvailabilityValue) VALUES ('Example', '2023-01-01', '2023-01-02', 0);

-- SELECT * FROM UserSchedules
-- WHERE UserName = 'Example' AND StartTime >= '2022-01-01 00:00:00' AND EndTime <= '2023-01-03 00:00:00';

-- SELECT DISTINCT(UserName) FROM UserSchedules; 

-- CALL usp_AddMeetingTime('Matthew', '2023-01-01 10:00', '2023-01-01 12:00', 1);