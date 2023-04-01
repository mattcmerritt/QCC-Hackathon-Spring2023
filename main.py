# SQL Backend
import mysql.connector

# UI
import tkinter
from tkinter import *
from tkinter import ttk
from datetime import datetime

def connect_to_server(user, password):
    return mysql.connector.connect(user=user, passwd=password, host='localhost', database='schedules')

def CheckMeetingTime(cursor, users, start, end):
    for user in users:
        cursor.callproc('usp_GetUserScheduleEntriesInRange', (user, start, end))
        for results in cursor.stored_results():
            print(results)

if (__name__ == "__main__"):
    # Connection
    # TODO: REMOVE USER INFORMATION BEFORE COMMITS!
    connection = connect_to_server('application', 'Requesting10Schedule!')
    cursor = connection.cursor()

    cursor.callproc('usp_GetAllUsers')

    # Listing out current team members
    members_list = []
    for results in cursor.stored_results():
        for name in results:
            members_list.append(name[0])
    print(members_list)

    # Setting Up Window
    curr_datetime = datetime.now()
    window = tkinter.Tk()
    window.geometry("500x500")

    # Title
    title = tkinter.Label(window, text="Schedule a Meeting", font=('Arial', 20))
    title.pack()
    line = ttk.Separator(window, orient=HORIZONTAL)
    line.pack(fill='x')

    # Creating Lists
    priority_value = range(1,6)
    window.members_dict = {}
    days_list = range(1,31)
    time_list = []
    count = 16
    time = 8
    while (count > 0):
        if (count % 2 == 0):
            time_list.append(str(time) + ':00 - ' + str(time) + ':30')
        else:
            time2 = time + 1
            time_list.append(str(time) + ':30 - ' + str(time2) + ':00')
            time = time + 1
        count = count - 1

    # MEMBERS: Labeling
    membersNeededLabel = tkinter.Label(window, text="Members Attending:", font=('Arial', 10))
    membersNeededLabel.pack()

    # MEMBERS: Inputting into lists with checkbuttons of members in the meeting
    for i, member in enumerate(members_list):
        window.members_dict[member] = Checkbutton(window, text=member)      # Set text for chechbutton
        window.members_dict[member].var = IntVar()                          # New IntVar for each member
        window.members_dict[member]['variable'] = window.members_dict[member].var
        window.members_dict[member].pack()

    # DAYS: Labeling
    dateLabel = tkinter.Label(window, text="Date:", font=('Arial', 10))
    dateLabel.pack()

    # DAYS: 
    window.var = IntVar()
    window.var.set(curr_datetime.day)
    window.dayOfMeeting = OptionMenu(window, window.var, *days_list)
    window.dayOfMeeting.pack()

    # TIME: Labeling
    timeLabel = tkinter.Label(window, text="Time:", font=('Arial', 10))
    timeLabel.pack()

    # TIME:
    window.var = IntVar()
    curr_time = curr_datetime.minute
    nextAvailableMeetingTime = ""
    if (curr_time < 15):
        nextAvailableMeetingTime = str(curr_datetime.hour) + ':00 - ' + str(curr_datetime.hour) + ':30'
    else:
        nextAvailableMeetingTime = str(curr_datetime.hour) + ':30 - ' + str(curr_datetime.hour + 1) + ':00'
    window.var.set(nextAvailableMeetingTime)
    window.timeOfMeeting = OptionMenu(window, window.var, *time_list)
    window.timeOfMeeting.pack()

    # PRIORITY: Labeling
    timeLabel = tkinter.Label(window, text="Priority:", font=('Arial', 10))
    timeLabel.pack()

    # PRIORITY: 
    window.var = IntVar()
    window.var.set(1)
    window.timeOfMeeting = OptionMenu(window, window.var, *priority_value)
    window.timeOfMeeting.pack()

    ## SCHEDULE BUTTON
    def check_schedule():
        CheckMeetingTime(cursor, ['Matthew', 'Example'], '2022-01-01 00:00:00', '2022-01-01 00:00:00')

    schedule_button = Button(window, text='Check Schedule', bd='5', command=check_schedule)
    schedule_button.pack()

    window.mainloop()

    cursor.close()
    connection.close()