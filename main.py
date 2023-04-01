import mysql.connector

def connect_to_server(user, password):
    return mysql.connector.connect(user=user, passwd=password, host='localhost', database='schedules')


if (__name__ == "__main__"):
    connection = connect_to_server('', '')
    cursor = connection.cursor()

    cursor.callproc('usp_GetAllScheduleEntries')

    for result in cursor.stored_results():
        print(result.fetchall())

    cursor.close()
    connection.close()