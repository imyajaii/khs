import datetime

# Get current date
now = datetime.datetime.now()
format_now = now.strftime("%m/%d/%Y %H:%M:%S")

print(f"Current date: {format_now}")