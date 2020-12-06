import sqlite3
conn = sqlite3.connect('example.db')

# 获取游标，代表内存中数据
c = conn.cursor()

def printData():
  c.execute("select * from stocks")
  for row in c:
    print(row)


print("Create table")
c.execute("DROP TABLE stocks")

c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

print('insert some')
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
c.execute("INSERT INTO stocks VALUES ('2006-01-05','SALE','RHAT',105,35.64)")
print('insert many')
sample = [
    ("2006-01-05","BUY","RHAT",100,35.14),
    ("2006-01-05","BUY","RHAT",100,35.14)
    ]
c.executemany("INSERT INTO stocks (date, trans, symbol, qty, price) VALUES (?,?,?,?,?)", sample)
conn.commit()
printData()

print('update some') 
c.execute("UPDATE stocks set trans='SALE' where price > 35.50 ")
# Save (commit) the changes
conn.commit()
printData()

# delete some 
print('delete some')
c.execute("delete from stocks where price=35.64")
conn.commit()
printData()

conn.close()