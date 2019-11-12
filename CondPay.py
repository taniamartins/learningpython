#chapter 3 - https://bit.ly/33TC1rS

xh = input ("Enter Hours:")
xr = input ("Enter Rate:")
fh = float(xh)
fr = float(xr)

if fh > 40 :
    reg = fh * fr
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else :
    xp = fh * fr
print ("Your pay is", xp)