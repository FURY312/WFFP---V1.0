from cgi import print_form
import urllib.request
import time


import urllib.request
import time

now = time
y= now.localtime().tm_year
m=now.localtime().tm_mon
d=now.localtime().tm_mday
h=now.localtime().tm_hour

a=y,m,d #년, 월, 일 data2 
data=str(a)
data_split = data.split(',')
data_join = ''.join(data_split)
data1=data_join.strip('() ')
data2=data1.replace(' ', '')
print(data2)


data3=str(h) #시간 data6 
data6=str(h)
if (h<10):
    h2=0,h
    data3=str(h2)
    data4=data3.strip('() ')
    data5=data4.replace(',', '')
    data6=data5.replace(' ', '')
print(data6)

data7=int(data6)
data8=data7-7
data9=str(data8)

#정시간
url1 = ('http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey=kFg3740w8oA0URfa6U0acwTHl6OBznrukbTSF5qHxgELxjG2jtx2Z7ozqItFCHb%2FLTqdMYBKqbgoJyxHQSDatA%3D%3D&numOfRows=4&pageNo=1&base_date='+data2+'&base_time='+data9+'00&nx=62&ny=125')

savename = "test.txt"

urllib.request.urlretrieve(url1, savename)