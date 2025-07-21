hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Invalid input: enter numerical value")
    quit()

nr = 1.5 * r
pay = 40 * r
if h <= 40 :
    pay = h * r
    print(pay)
elif h > 40 :
    ot = h - 40
    np = ot * nr
    pay = pay + np
    print(pay)

