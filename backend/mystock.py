import random as rand
from datetime import datetime  
from datetime import timedelta  

date=datetime(2003,8,22)
price=1000
f=open('stock.csv','w')
while date!= datetime(2018,1,12):
    d=rand.randint(1,2)
    if d==1:
        price+=rand.randint(0,3)
    elif d==2:
        price-=rand.randint(0,2)
    f.write(date.strftime('%m/%d/%Y %H:00')+','+str(price)+'\n')
    date += timedelta(hours=1)

f.close()
print(price)
