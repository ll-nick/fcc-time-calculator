weekdays = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday"
]

def add_time(start, duration, weekday = None):
    start_am = True if start.split()[1] == "AM" else False
    start_hours, start_minutes = [int(str) for str in start.split()[0].split(":")]

    start_acc = start_hours if start_am else start_hours + 12
    start_acc *= 60
    start_acc += start_minutes

    duration_hours, duration_minutes = [int(str) for str in duration.split(":")]
    duration_acc = duration_hours * 60 + duration_minutes
    new_time_acc = start_acc + duration_acc

    new_time_hours = new_time_acc // 60
    new_time_minutes = new_time_acc % 60

    new_time_days = new_time_hours // 24
    new_time_hours -= new_time_days * 24

    new_time_am = " AM"
    if new_time_hours >= 12:
        new_time_am = " PM"
        if new_time_hours > 12:
            new_time_hours -= 12
    if new_time_hours == 0:
        new_time_hours = 12

    offset = ""
    if new_time_days >= 2:
        offset = " (" + str(new_time_days) + " days later)"
    elif new_time_days >= 1:
        offset = " (next day)"
    
    new_weekday = ""
    if weekday is not None:
        weekday_number = weekdays.index(weekday.lower())
        weekday_number += new_time_days
        weekday_number = weekday_number % 7
        new_weekday = weekdays[weekday_number]
        new_weekday = ", " + new_weekday.capitalize()

    new_time_minutes_str = ("0" + str(new_time_minutes))[-2:]
    return str(new_time_hours) + ":" + new_time_minutes_str + new_time_am + new_weekday + offset