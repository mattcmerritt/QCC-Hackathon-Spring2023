CREATE PROCEDURE usp_GetAllScheduleEntries()
	SELECT * FROM UserSchedules;
    
CALL usp_GetAllScheduleEntries