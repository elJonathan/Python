hrs = input("Enter Hours:")
rate = input("Enter rate")
h = float(hrs)
r = float(rate)

def computepay(h,r):
    if h <= 40:
        pay = h * r
        return pay
    elif h > 40:
        pay = (40 * r) + (1.5 * r * (h - 40))
        return pay

p = computepay(h,r)
print("Pay",p)
