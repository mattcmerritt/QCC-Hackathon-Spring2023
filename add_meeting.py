from tkinter import *
from tkinter.ttk import *

window = Tk()
window.geometry("750x500")

times = []

# 8:00 to 4:00 (16:00)
time = 8
mins = ":00"
while (time <= 16):
    times.append(str(time) + mins);
    if(mins == ':00' and time != 16):
        mins = ":30"
    else:
        mins = ":00"
        time += 1

days = []
for i in range(1, 31):
    days.append(str(i))

# days = [
#     "Sunday",
#     "Monday",
#     "Tuesday",
#     "Wednesday",
#     "Thursday",
#     "Friday",
#     "Saturday"
# ]

priorities = [
    "1",
    "2",
    "3",
    "4",
    "5"
]

entry_usernames = []
entry_days = []
entry_starts = []
entry_ends = []
entry_priorities = []

def create_entry_ui():
    # user
    entry_usernames.append(StringVar())
    u_entry = Entry(window, textvariable=entry_usernames[len(entry_usernames)-1])
    u_entry.grid(row=len(entry_usernames)+1, column=0)

    # day
    entry_days.append(StringVar())
    d_dropdown = Combobox(window, values=days, textvariable=entry_days[len(entry_days)-1], width=20)
    d_dropdown.grid(row=len(entry_days)+1, column=1)

    # start
    entry_starts.append(StringVar())
    s_dropdown = Combobox(window, values=times, textvariable=entry_starts[len(entry_starts)-1], width=20)
    s_dropdown.grid(row=len(entry_starts)+1, column=2)

    # ends
    entry_ends.append(StringVar())
    e_dropdown = Combobox(window, values=times, textvariable=entry_ends[len(entry_ends)-1], width=20)
    e_dropdown.grid(row=len(entry_ends)+1, column=3)

    # prio
    entry_priorities.append(StringVar())
    p_dropdown = Combobox(window, values=priorities, textvariable=entry_priorities[len(entry_priorities)-1], width=20)
    p_dropdown.grid(row=len(entry_priorities)+1, column=4)

def save_all_entries():
    for i in range(0, len(entry_usernames)):
        f_day = str(entry_days[i])
        if(len(f_day) == 1):
            f_day = "0" + f_day
        
        f_start_time = str(entry_starts[i])
        if(len(f_start_time) == 4):
            f_start_time = "0" + f_start_time

        f_end_time = str(entry_ends[i])
        if(len(f_end_time) == 4):
            f_end_time = "0" + f_end_time

        f_start_date = "2023-04-" + f_day + " " + f_start_time + ":00"
        f_end_date = "2023-04-" + f_day + " " + f_end_time + ":00"

        cursor.callproc("usp_AddMeetingTime", (entry_usernames[i], f_start_date, f_end_date, entry_priorities[i]))

add_entry_button = Button(window, text="Add entry", command=create_entry_ui, width=20)
save_button = Button(window, text="Save", command=save_all_entries, width=20)

add_entry_button.grid(row=0, column=0)
save_button.grid(row=0, column=1)

username = Label(window, text="Username", width=20)
username.grid(row=1, column=0)
day = Label(window, text="Date", width=20)
day.grid(row=1, column=1)
start = Label(window, text="Start Time", width=20)
start.grid(row=1, column=2)
end = Label(window, text="End Time", width=20)
end.grid(row=1, column=3)
priority = Label(window, text="Priority", width=20)
priority.grid(row=1, column=4)

window.mainloop()
