#strftime:This method is calls and takes parameter, format , to specify the format of returned string.
#%b ->Month name ,Short Version. ex:Dec
#%B ->Month name,Full version. Ex: December
#%m ->Month as number .ex:01-12     12
#%y ->year short version,without century.  ex:18
#%Y ->year,full Version. Ex:2018
#%H ->Hour.Ex:00-23
#%I ->Hour.Ex:00-12
#%p ->AM/pm
#%M ->Minutes. ex:00-59 
#%S ->Second
#%a ->Abbreviated weekday name
#%A ->Full weekday name
#%w ->Weekday as a decimal number
#%d ->Day of the month as a zero-padded decimal  01, 02, ..., 31
#%-d ->Day of the month as a decimal number  1, 2, ..., 30


import datetime as d

n = d.datetime.now()
print(n)

E = n.strftime("%H")
print("Hour(24):", E)
print('Hour(12):', n.strftime('%I'))
print('AM/PM:', n.strftime('%p'))

a = n.strftime("%M")
print("Minutes: ",a)

st = n.strftime("%S")
print("Seconds: ", st)

print("Month name:", n.strftime('%b'))
print("Month name:", n.strftime('%B'))
print('Month:', n.strftime('%m'))

print('Year:', n.strftime('%y'))
print('Year:', n.strftime('%Y'))

print(n.strftime('%I:%M:%S %p'))

