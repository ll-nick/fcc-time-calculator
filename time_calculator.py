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
    start_24h = to_24_hour_format(start)
    start_int = time_str_to_int(start_24h)
    duration_int = time_str_to_int(duration)

    new_time_int = start_int + duration_int

    new_time_hours = new_time_int // 60
    new_time_minutes = new_time_int % 60

    new_time_days = new_time_hours // 24
    new_time_hours -= new_time_days * 24

    offset = offset_str(new_time_days)
    offset_spacing = " " if offset != "" else ""
    new_weekday = get_new_weekday(weekday, new_time_days)
    weekday_spacing = ", " if new_weekday != "" else ""

    new_time_str_24h = str(new_time_hours) + ":" + two_digit_string(new_time_minutes)
    new_time_str_12h = to_12_hour_format(new_time_str_24h)
    new_time_str = new_time_str_12h + \
                    weekday_spacing + new_weekday + \
                    offset_spacing + offset
    
    return new_time_str

def to_24_hour_format(time_str):
    if time_str.split()[1] == "PM":
        time_str = add_12_hours(time_str)
    return time_str.split()[0]

def to_12_hour_format(time_str):
    hour, minute = [int(str) for str in time_str.split(":")]

    suffix = "AM"
    if hour >= 12:
        suffix = "PM"
        hour -= 12
    if hour == 0:
        hour = 12

    return str(hour) + ":" + two_digit_string(minute) + " " + suffix

def add_12_hours(time_str):
    return str(int(time_str.split(':')[0]) + 12) + ":" + time_str.split(':')[1]

def time_str_to_int(time_str):
    hours, minutes = [int(str) for str in time_str.split(":")]
    return hours * 60 + minutes

def offset_str(offset_days):
    if offset_days >= 2:
        return "(" + str(offset_days) + " days later)"
    elif offset_days >= 1:
        return "(next day)"
    return ""
    
def get_new_weekday(weekday, days_offset):
    if weekday is None:
        return ""
    
    weekday_number = weekdays.index(weekday.lower())
    weekday_number += days_offset
    weekday_number = weekday_number % 7
    return weekdays[weekday_number].capitalize()

def two_digit_string(input):
    return ("0" + str(input))[-2:]

