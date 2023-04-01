CREATE PROCEDURE usp_GetAllScheduleEntries()
	SELECT * FROM UserSchedules;
    
-- CALL usp_GetAllScheduleEntries;

CREATE PROCEDURE usp_AddMeetingTime(userName VARCHAR(50), startTime DATETIME, endTime DATETIME, availabilityValue INT)
	INSERT INTO UserSchedules VALUES (userName, startTime, endTime, availabilityValue);
    
CALL usp_AddMeetingTime('Michael', '2023-01-01 10:00', '2023-01-01 12:00', 1);

DROP PROCEDURE usp_GetUserScheduleEntriesInRange;

CREATE PROCEDURE usp_GetUserScheduleEntriesInRange(uName VARCHAR(50), meetStart DATETIME, meetEnd DATETIME)
	SELECT * FROM UserSchedules
    WHERE UserName = uName AND NOT (StartTime > meetEnd OR EndTime < meetStart);
    
-- CALL usp_GetUserScheduleEntriesInRange('Example 2', '2023-01-01 10:00', '2023-01-01 12:00');

CREATE PROCEDURE usp_GetAllUsers()
	SELECT DISTINCT(UserName) FROM UserSchedules;
    
-- CALL usp_GetAllUsers;