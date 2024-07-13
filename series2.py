import pandas as aj
cal={'day1':429,'day2':390,'day3':458}

myvar=aj.Series(cal)
print(myvar)
print('\n')

my=aj.Series(cal,['day1','day2'])
print(my)