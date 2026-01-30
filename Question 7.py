# Question 7

def convert_Seconds_To_Time(secondsSinceMidnight):
    if secondsSinceMidnight < 0 or secondsSinceMidnight > 86399:
        return "Invalid input: seconds must be between 0 and 86399."
    hours = secondsSinceMidnight // 3600
    minutes = (secondsSinceMidnight % 3600) // 60
    seconds = secondsSinceMidnight % 60

    if hours < 12:
        period = "AM"
    else:
        period = "PM"

    if hours == 0:
        hours = 12
    elif hours > 12:
        hours -= 12
    return f"{hours}h {minutes}m {seconds}s"
result = convert_Seconds_To_Time(7878)
print(result)