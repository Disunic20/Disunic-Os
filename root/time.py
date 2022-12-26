from datetime import datetime
from datetime import date
def time():
    now = datetime.now()
    current_time = now.strftime("%I:%M:%S")
    print("The current time is:",current_time,"Hour Minute Second")
def dates():
    today = date.today()
    print("The current date is:",today)
