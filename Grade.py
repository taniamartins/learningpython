#chapter 3 - https://bit.ly/33TC1rS
x = input ("Enter Score:")

try:
    x = float(x)

    if x >= 0.9 :
        print('A')
    elif x >= 0.8 :
        print('B')
    elif x >= 0.7 :
        print('C')
    elif x >= 0.6 :
        print('D')
    elif x < 0.6 :
        print('F')

except:
    print ("Please input a number")