import random
from datetime import datetime, timedelta

def get_Random_date(start_date, end_date):
    start = datetime.strptime(start_date, '%m/%d/%Y')
    end = datetime.strptime(end_date, '%m/%d/%Y')
    print(start)
    print(end)


    delta_days = (end - start).days
    print(delta_days)
    random_days = random.randint(0 , delta_days)


    return (start + timedelta(days=random_days)).strftime("%m/%d/%Y")



print("Random Date =", get_Random_date("1/1/2016", "12/12/2018"))