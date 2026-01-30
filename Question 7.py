# Question 7

def convert_Seconds_To_Time(secondsSinceMidnight):
    # Validate that the input is within the valid range for a day
    if secondsSinceMidnight < 0 or secondsSinceMidnight > 86399:
        return "Invalid input: seconds must be between 0 and 86399."
    # Calculates hours,minutes, and seconds
    hours = secondsSinceMidnight // 3600
    minutes = (secondsSinceMidnight % 3600) // 60
    seconds = secondsSinceMidnight % 60
    # Determines whether the time is am or pm
    if hours < 12:
        period = "AM"
    else:
        period = "PM"
    # Convert from 24-hour time to a 12 hour time format
    if hours == 0:
        hours = 12
    elif hours > 12:
        hours -= 12
    return f"{hours}h {minutes}m {seconds}s"
result = convert_Seconds_To_Time(8888)
print(result)