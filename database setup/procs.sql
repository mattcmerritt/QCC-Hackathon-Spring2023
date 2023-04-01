CREATE PROCEDURE usp_GetAllScheduleEntries()
	SELECT * FROM UserSchedules;
    
-- CALL usp_GetAllScheduleEntries;

CREATE PROCEDURE usp_AddMeetingTime(userName VARCHAR(50), startTime DATETIME, endTime DATETIME, availabilityValue INT)
	INSERT INTO UserSchedules VALUES (userName, startTime, endTime, availabilityValue);
    
-- CALL usp_AddMeetingTime('Example 2', '2023-01-01 10:00', '2023-01-01 12:00', 1);

CREATE PROCEDURE usp_GetUserScheduleEntriesInRange(uName VARCHAR(50), startT DATETIME, endT DATETIME)
	SELECT * FROM UserSchedules
    WHERE UserName = uName AND StartTime >= startT AND EndTime <= endT;
    
-- CALL usp_GetUserScheduleEntriesInRange('Example 2', '2023-01-01 10:00', '2023-01-01 12:00');