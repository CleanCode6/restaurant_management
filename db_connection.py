import pymysql

from model.restaurants import Restaurants


class DBConnection:
	def __init__(self):
		# self.DB = pymysql.connect(
		# 		user='root', 
		# 		passwd='1234', 
		# 		host='localhost', 
		# 		port=3306,
		# 		db='Restaurants', 
		# 		charset='utf8',
		# 		cursorclass=pymysql.cursors.DictCursor
		# 	)
		self.DB = pymysql.connect(
				user='cau', 
				passwd='kG6byywEExRr', 
				host='3.35.49.232', 
				# port=,
				db='Restaurants', 
				charset='utf8',
				cursorclass=pymysql.cursors.DictCursor
			)


	def get_restaurants(self):
		cursor = self.DB.cursor()
		QUERY = "SELECT * FROM Restaurants;"
		cursor.execute(QUERY)
		result = cursor.fetchall()
		return result

	def get_restaurant(self, restaurant_id):
		cursor = self.DB.cursor()
		QUERY = f"SELECT * FROM Restaurants WHERE restaurant_id ='{restaurant_id}';"
		cursor.execute(QUERY)
		result = cursor.fetchall()
		print('db: \n', result)
		print(type(result))
		if len(result) > 0:
			return result[0]
		else:
			return None

	def register_restaurant(self, rest_query):  
		cursor = self.DB.cursor()
		placeholders = ', '.join(['%s'] * len(rest_query))
		columns = ', '.join(rest_query.keys())
		values = list(rest_query.values())
		QUERY = "INSERT INTO Restaurants (%s) VALUES (%s);" % (columns, placeholders)
		cursor.execute(QUERY, values)
		self.DB.commit()

	def update_restaurant(self, rest_query, restaurant_id):
		cursor = self.DB.cursor()
		result_str = self.make_update_query(rest_query)
		QUERY = "UPDATE Restaurants SET %s WHERE restaurant_id ='%s';" % (result_str, restaurant_id)
		cursor.execute(QUERY)
		self.DB.commit()

	
	def delete_restaurant(self, restaurant_id):
		cursor = self.DB.cursor()
		QUERY = f"DELETE FROM Restaurants WHERE restaurant_id='{restaurant_id}';"
		cursor.execute(QUERY)
		self.DB.commit()

	def rollback(self):
		self.DB.rollback()
		self.DB.close()

	def close_connection(self):
		self.DB.close()