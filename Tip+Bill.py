def total_calc(bill_amount,tip_amount):
    #define function to calculate the tip on the bill
    total = bill_amount*(1+0.01*tip_amount)
    total = round(total, 2)
    print(f"Please pay ${total}")

# specify only bill_amount
# default value of tip percentage is used

total_calc(150,20)

# define function to calculate cube

def cube(number):
    return number*number*number


# define a function that will execute cube function if the user entered the number is divisible by 3
def by_three(number):
    if number %3 ==0:
        return cube(number)
    else:
        return False
    
#display result
print(by_three(9))
print(by_three(4))