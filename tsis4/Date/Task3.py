import datetime

dt_with_microseconds = datetime.datetime.now()

dt_without_microseconds = dt_with_microseconds.replace(microsecond=0)

print("Datetime with microseconds:", dt_with_microseconds)
print("Datetime without microseconds:", dt_without_microseconds)
