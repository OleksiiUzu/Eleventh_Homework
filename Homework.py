import datetime
import random


# creates a list from "08:00" to "18:00"
def time_check():
    time_range_list = []
    for hour in range(8, 18):
        hour = str(hour).zfill(2)
        for minute in range(0, 60, 15):
            minute = str(minute).zfill(2)
            time = f'{hour}:{minute}'
            time_range_list.append(time)
    time_range_list.append('18:00')
    return time_range_list


def time_to_str(lst: list, index: int):
    # returns a str (datetime.hour and .minute method filled with 0)
    return f'{str(lst[0][index].hour).zfill(2)}:{str(lst[0][index].minute).zfill(2)}'


def register_to_visit_time(time_range: list, spend_time):
    start_time = time_to_str(time_range, 0)  # example: 08:00
    end_time = time_to_str(time_range, 1)  # example: 09:00
    t = time_check()  # ['08:00', '08:15', ..., '17:45', '18:00']

    start = t.index(start_time)
    end = t.index(end_time)+1
    base_list = t[start:end]

    time_to_return = t[start+(spend_time*4):end+(spend_time*4)]
    time_to_visit = base_list[:len(time_to_return)]
    if not time_to_return and not time_to_visit:
        return None
    else:
        return time_to_visit, time_to_return


if __name__ == '__main__':
    x = [
        [(datetime.datetime(2023, 8, 1, 8, 0), datetime.datetime(2023, 8, 1, 9, 0),)],
        [(datetime.datetime(2023, 8, 1, 12, 0), datetime.datetime(2023, 8, 1, 16, 0),)],
        [(datetime.datetime(2023, 8, 1, 13, 0), datetime.datetime(2023, 8, 1, 18, 0),)],
        [(datetime.datetime(2023, 8, 1, 16, 0), datetime.datetime(2023, 8, 1, 17, 0),)],
        [(datetime.datetime(2023, 8, 1, 18, 0), datetime.datetime(2023, 8, 1, 18, 0),)],
        [(datetime.datetime(2023, 8, 1, 8, 0), datetime.datetime(2023, 8, 1, 18, 0),)],
        [(datetime.datetime(2023, 8, 1, 12, 0), datetime.datetime(2023, 8, 1, 15, 0),)],
        [(datetime.datetime(2023, 8, 1, 10, 0), datetime.datetime(2023, 8, 1, 16, 0),)]
        ]

    for time in x:
        y = random.randint(1, 12)
        result = register_to_visit_time(time, y)
        print(f'\nSpend time: {y} hour(s)')
        if result:
            print('Time to visit:')
            print(result[0])
            print('Time to return:')
            print(result[1])
        else:
            print("Invalid spend time!")
