#chapter 4: https://bit.ly/2rPydtH
def computepay (hours, rate) :
    #print ('In computepay', hours, rate)
    if hours > 40 :
        reg = hours * rate
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp
    else :
        pay = hours * rate
    #print ("Your pay is", pay)
    return pay

xh = input ("Enter Hours:")
xr = input ("Enter Rate:")
fh = float(xh)
fr = float(xr)

xp = computepay (fh, fr)
print ('Your pay is', xp)