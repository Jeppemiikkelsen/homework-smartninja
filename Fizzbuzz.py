#i stedet for at bruger indtaster nummer, så har jeg brugt random
import random
number = random.randint(1,100)
count=0
while count!=number:
    if count%3==0 and count%5==0:
        print("fizzbuzz")
        count = (count + 1)
    elif count%3==0:
        print("fizz")
        count = (count + 1)
    elif count%5==0:
        print("buzz")
        count = (count + 1)
    else:
        print(count)
        count = (count + 1)
