# Database program to access mysql tables on command prompt - SUCCESSFUL
import pymysql
conn=pymysql.connect(host='localhost', user='root', password='', db='empdb')
a=conn.cursor()
sql='SELECT * from empdet'; 
a.execute(sql)
countrow=a.execute(sql)
print("no of rows:", countrow)
data=a.fetchone()
print(data) 
