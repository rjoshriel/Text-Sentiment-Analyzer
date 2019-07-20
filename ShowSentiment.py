
import sqlite3

class loginDAL(object):

	def show_positive(self,user):

		conn=sqlite3.connect('products.db')
		cursor=conn.cursor
		print ("Showing Positive feedbacks")
		cursor=conn.execute ("SELECT * from Reviews WHERE rating>=3 ORDER BY rating desc")
		print("Name\t\tRating\tReview")
		for row in cursor:
			print row[0],"\t\t",row[1],"\t",row[2]
		conn.commit()
		conn.close()
	
	def show_nega(self,user):
	
		cursor=conn.cursor
		print ("\nShowing Negative feedbacks")
		cursor=conn.execute ("SELECT * from Reviews WHERE rating<3 ORDER BY rating desc")
		print("Name\t\tRating\tReview")
		for row in cursor:
			print row[0],"\t\t",row[1],"\t",row[2]

		conn.cursor()
		conn.close


	



