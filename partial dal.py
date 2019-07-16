import sqlite3


conn=sqlite3.connect('products.db')
cursor=conn.cursor()

print("Opened Database Successfully!")

cursor=conn.execute("SELECT Name, rating, review from Reviews")

for row in cursor:
	print ("NAME = "), row[0]
	print ("Rating Given = "), row[1]
	print ("Review : "), row[2]
	print ("\n")

print ("Operation done successfully!");
conn.close
