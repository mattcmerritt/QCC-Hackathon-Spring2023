# Setting Up Window
import tkinter
from tkinter import *
from tkinter import ttk
from datetime import datetime
curr_datetime = datetime.now()
window = tkinter.Tk()
window.geometry("500x500")

# Title
title = tkinter.Label(window, text="Schedule a Meeting", font=('Arial', 20))
title.pack()
line = ttk.Separator(window, orient=HORIZONTAL)
line.pack(fill='x')

# Creating Lists
members_list = ["Micheal", "Matthew", "Ty"]
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
def checkMembers():
    print("got through")
    for result in window.members_dict.values():
        if result.var.get():
            print(format(result['text']))

# DAYS: Labeling
dateLabel = tkinter.Label(window, text="Date:", font=('Arial', 10))
dateLabel.pack()

# DAYS: TO GET DAY USE day_selected
day_selected = IntVar()
day_selected.set(curr_datetime.day)
window.dayOfMeeting = OptionMenu(window, day_selected, *days_list)
window.dayOfMeeting.pack()

# TIME: Labeling
timeLabel = tkinter.Label(window, text="Time:", font=('Arial', 10))
timeLabel.pack()

# TIME: TO GET SELECTED TIME USE nextAvailableMeetingTime
time_selected = IntVar()
curr_time = curr_datetime.minute
nextAvailableMeetingTime = ""
if (curr_time < 15):
    nextAvailableMeetingTime = str(curr_datetime.hour) + ':00 - ' + str(curr_datetime.hour) + ':30'
else:
    nextAvailableMeetingTime = str(curr_datetime.hour) + ':30 - ' + str(curr_datetime.hour + 1) + ':00'
time_selected.set(nextAvailableMeetingTime)
window.timeOfMeeting = OptionMenu(window, time_selected, *time_list)
window.timeOfMeeting.pack()

def getEverything():
    print(time_selected)
    print(time)
    print(day_selected.get())
    checkMembers()

## Check BUTTON
check_availability = Button(window, text='Check Availability', bd='5', command=getEverything)
check_availability.pack()





window.mainloop()