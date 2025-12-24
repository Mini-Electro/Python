vaild = False
while not vaild:
    try:
        n=int(input("Enter a number: "))
        #enter an even number
        while n%2==0:
            print("bye")
        vaild = True
    except ValueError:
        print("Invaild")