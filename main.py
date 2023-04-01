import pymysql

def connect_to_server(user, password) -> pymysql.connections.Connection:
    return pymysql.connect(db='schedules', user=user, passwd=password, host='localhost', port=3306)


if (__name__ == "__main__"):
    connection = connect_to_server('', '')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM UserSchedules')

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    connection.close()