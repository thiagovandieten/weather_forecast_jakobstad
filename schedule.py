def get_schedule():
    try:
        schedule_file = open('schedule.txt', 'r')
        schedule = schedule_file.read()
        schedule_file.close()
        return schedule

    except FileNotFoundError as err:
        print(err)
