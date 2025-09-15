#nested condition nothing but the condition inside the condition
#match-------->introduced in the 3.10 version

'''
if condition:
  if condition:
    block of code
  else:
    block of code
else:
 block of code
'''
s=input('Enter your location')
modeofTran=input('Enter the mode of transport')
if s=='reached':
    if modeofTran=='metro':
        print('reached home through metro')
    else:
        print('reached home by bus')
else:
    print('still on the way')

#leap year


year = int(input('enter year'))

if year%400==0:
    print(year,'is a leap year')
elif year%100==0:
    print(year,'is not a leap year')
elif year%4==0:
    print(year,'is a leap year')
else:
    print('is not leap year')

