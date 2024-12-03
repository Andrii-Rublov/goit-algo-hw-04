
# the function is to calculate total and average salary

# def total_salary(path):
#     try:
#         salary = list()
#         with open(path, "r", encoding="utf-8") as salary_bill:
#             lines = [el.strip() for el in salary_bill.readlines()] #Removing whitespace chars from lines
#             for line in lines:
#                 salary.append(line.split(',')[1]) #take out salary amounts (string format) from file and add them to list
#                 salary = [int(x) for x in salary] #converting string format to integers
#                 total = sum(salary) #calculating total amount of the salary
#                 average = int(total / len(salary)) #calculating average amount of the salary
#             print(f"Total amount of salary: {total}, Average salary: {average}")
#     except FileNotFoundError:
#         print(f"File {path} is not found.")
#     except OSError:
#         print(f"File {path} is corrupted or cannot be read.")
#
#
# #Check the function:
# total_salary("TextFiles/salary_file.txt") #Valid input
# total_salary("salary.txt") #Invalid input

from datetime import datetime, date, timedelta


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def date_to_string(date):
    return date.strftime("%Y.%m.%d")


def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list


def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)


def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:
        return find_next_weekday(birthday, 0)
    return birthday


def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()

    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)

        """
        Додайте на цьому місці перевірку, чи не буде 
        припадати день народження вже наступного року.
        """
        if birthday_this_year < today:
            birthday_this_year = user["birthday"].replace(year=today.year + 1)

        if 0 <= (birthday_this_year - today).days <= days:
            """ 
            Додайте перенесення дати привітання на наступний робочий день,
            якщо день народження припадає на вихідний. 
            """
        if birthday_this_year.weekday() >= 5:
            birthday_this_year = find_next_weekday(birthday_this_year, 0)
        else:
            birthday_this_year

        congratulation_date_str = date_to_string(birthday_this_year)
        upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})
    return upcoming_birthdays

