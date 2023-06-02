# Meetup

from datetime import datetime, date
from calendar import monthrange

# subclassing the build-in ValueError to create MeetupDayException


class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in valid date.
    message: explanation of the error.
    """

    def __init__(self, message):
        self.message = message


DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
WEEK = ["first", "second", "third", "forth", "fifth"]


def meetup(year, month, week, day_of_week):
    first_day_index = DAYS.index(datetime(year, month, 1).strftime("%A"))
    first_teen_index = DAYS.index(datetime(year, month, 13).strftime("%A"))
    first_last_day_index = (
        DAYS.index(
            datetime(
                year if month < 12 else year + 1, month + 1 if month < 12 else 1, 1
            ).strftime("%A")
        )
        - 8
    ) % 7
    target_index = DAYS.index(day_of_week)
    if week == "teenth":
        delta = (
            target_index - first_teen_index
            if target_index >= first_teen_index
            else 7 - (first_teen_index - target_index)
        )
        target_day = 13 + delta
    elif week == "last":
        delta = (
            target_index - first_last_day_index
            if target_index >= first_last_day_index
            else 7 - (first_last_day_index - target_index)
        )
        target_day = (
            (monthrange(year, month)[1] - 7) + delta
            if delta > 0
            else monthrange(year, month)[1]
        )
    else:
        delta = (
            target_index - first_day_index
            if target_index >= first_day_index
            else 7 - (first_day_index - target_index)
        )
        target_day = (1 + WEEK.index(week) * 7) + delta

    try:
        out = print(
            "Your meetup is: ", date(year, month, target_day)
        )  # for VSCode test only
        return out
    except:
        raise MeetupDayException("That day doesn't exist.")


meetup(2023, 6, "teenth", "Monday")
# meetup(2023, 6, "fifth", "Sunday") # error to check if Exception works
meetup(2023, 6, "last", "Friday")
meetup(2023, 6, "first", "Tuesday")
