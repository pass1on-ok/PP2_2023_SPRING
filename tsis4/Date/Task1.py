import datetime


current_date = datetime.date.today()


new_date = current_date - datetime.timedelta(days=5)


print("Today:",current_date,'\nFive days before today was:', new_date)
