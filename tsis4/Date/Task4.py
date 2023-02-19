from datetime import datetime

def date_difference_seconds(date1, date2):
    
    # Convert date strings to datetime objects
    dt1 = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
    dt2 = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')
    
    # Calculate the difference in seconds
    diff_seconds = (dt2 - dt1).total_seconds()
    
    return diff_seconds

# Example usage
date1 = input('1st date: ')
date2 = input('2nd date: ')

diff_seconds = date_difference_seconds(date1, date2)
print("The difference between {date1} and {date2} is {diff_seconds} seconds.".format(date1 = date1,date2=date2,diff_seconds=diff_seconds))
