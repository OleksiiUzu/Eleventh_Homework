# Datetime-schedule

Write a function that calculates available time slots for booking an appointment for an animal. The time step is 15 minutes (meaning you can book at times like 10:00, 10:15, 10:30, and so on).

Input parameters:

A list of pairs representing the start and end of reserved times.

The desired duration of the visit.

For example:

f(x, y)

Where:

x = [(datetime.datetime(2023, 08, 01, 08, 0), datetime.datetime(2023, 08, 01, 09, 0))]

y = 2

The result should be a list of available time slots for booking.

For example: ["9:00", "9:15", "9:30", ...]

Consider that the shelter is open for visits from 8:00 to 18:00.

## Solution in new.py
