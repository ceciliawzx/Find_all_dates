from datetime import date, timedelta

weekdays: dict = {
    "monday": 0,
    "tuesday": 1,
    "wednesday": 2,
    "thursday": 3,
    "friday": 4,
    "saturday": 5,
    "sunday": 6,
}


def find_all_weekdays(start_date: date, end_date: date, weekday_name: str) -> list[date]:
    """
    Find all occurrences of a specific weekday within a date range.

    Args:
      start_date: The starting date (inclusive).
      end_date: The ending date (inclusive).
      weekday_name: The name of the weekday (e.g., "Monday").

    Returns:
      A list of dates on the given weekday within the date range.
    """
    weekday_num = weekdays[weekday_name.lower()]

    current_date = start_date
    all_weekdays = []
    while current_date <= end_date:
        if current_date.weekday() == weekday_num:
            all_weekdays.append(current_date)
        current_date += timedelta(days=1)

    return all_weekdays


# start_date = date(2023, 12, 18)  # Adjust these as needed
# end_date = date(2024, 1, 1)
# weekday_name = "Monday"
#
# all_mondays = find_all_weekdays(start_date, end_date, weekday_name)
#
# print(f"All {weekday_name}s within the range:")
# for monday in all_mondays:
#     print(monday)


def find_all_dates():
    stop = False
    start_date_list = None
    end_date_list = None
    while not stop:
        start_date_str = input("Please input the start date in format yyyy/mm/dd:\n")
        end_date_str = input("Please input the end date in format yyyy/mm/dd:\n")
        try:
            start_date_list = [int(part) for part in start_date_str.split("/")]
            end_date_list = [int(part) for part in end_date_str.split("/")]
            if len(start_date_list) == 3 and len(end_date_list) == 3:
                stop = True
            else:
                print("Wrong input, please try again.\n")
        except ValueError:
            print("Wrong input, please try again.\n")

    start_date = date(start_date_list[0], start_date_list[1], start_date_list[2])
    end_date = date(end_date_list[0], end_date_list[1], end_date_list[2])

    stop = False
    target_day = None
    while not stop:
        target_day_str = input("Please input target day: e.g Monday\n")
        if target_day_str.lower() in weekdays:
            target_day = target_day_str
            stop = True
        else:
            print("Please input a correct day.\n")

    res = find_all_weekdays(start_date, end_date, target_day)
    print(f"All {target_day}s within the range:")
    for res_date in res:
        print(res_date)


find_all_dates()
