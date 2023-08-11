weekdays = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday"
]

def add_12_hours(time_str):
    return str(int(time_str.split(':')[0]) + 12) + ":" + time_str.split(':')[1]

def to_24_hour_format(time_str):
    if time_str.split()[1] == "PM":
        time_str = add_12_hours(time_str)
    return time_str.split()[0]

def time_str_to_int(time_str):
    hours, minutes = [int(str) for str in time_str.split(":")]
    return hours * 60 + minutes

def add_time(start, duration, weekday = None):
    start_24h = to_24_hour_format(start)
    start_int = time_str_to_int(start_24h)
    duration_int = time_str_to_int(duration)

    new_time_int = start_int + duration_int

    new_time_hours = new_time_int // 60
    new_time_minutes = new_time_int % 60

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