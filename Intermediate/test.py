from datetime import datetime
t1="Sun 10 May 2015 13:54:36 -0700"
t2="Sun 10 May 2015 13:54:36 -0000"
months = {
   'Jan':'01',
   'Feb':'02',
   'Mar':'03',
   'Apr':'04',
   'May':'05',
   'Jun':'06',
   'Jul':'07',
   'Aug':'08',
   'Sep':'09',
   'Oct':'10',
   'Nov':'11',
   'Dec':'12'
    }
t1=t1.replace(t1[7:10], months[t1.split(' ')[2]])
t2=t2.replace(t2[7:10], months[t2.split(' ')[2]])
print(t1 + '\n'+ t2)
if ':' in str(datetime.strptime(t1[4:14], "%d %m %Y")-datetime.strptime(t2[4:14], "%d %m %Y")).split(' ')[0]:
    delta=0
else:
    print(str(((datetime.strptime(t1[4:14], "%d %m %Y")-datetime.strptime(t2[4:14], "%d %m %Y"))*86400)))