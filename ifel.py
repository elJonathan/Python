hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, Please enter numeric value")
    quit()


if h <= 40:
    pay = h * r
    print(pay)
elif h > 40:
    pay = (40 * r) + (1.5 * r * (h - 40))
    print(pay)
