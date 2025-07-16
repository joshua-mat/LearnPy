hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Invalid input")
    quit()

if h > 40 :
    reg = h * r
    ot = (h-40)*(r*0.5)
    xp = reg + ot
else:
    xp = h * r
print('pay',xp)

