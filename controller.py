from flask import flash
# from typing import List

from page_maker import PageMaker
from db_connection import DBConnection
# from model.restaurants import Parser

from forms import RestaurantForm


class Controller:
	def __init__(self):
		self.db = DBConnection()
		self.page_mk = PageMaker()
		self.db.connect_to_db()

	def restaurants_list_controller(self):
		rests_query = self.db.get_restaurants()
		self.db.close_connection()
		return self.page_mk.make_restautants_list_page(rests_query)
		
	def register_restaurant_controller(self, request):
		form = RestaurantForm()
		if form.validate_on_submit():
			rest_query = request.form.to_dict(flat=False)
			self.db.register_restaurant(rest_query)  
			self.db.close_connection()
			try:
				flash('Restaurant registered correctly', 'success')
				# 설계에는 없음..! 일단,,
				return self.restaurants_list_controller()
			except:
				self.db.rollback()
				flash('Error restaurant registeration.', 'danger')
		# get
		return self.page_mk.make_resgister_page(form)

	def update_restaurant_controller(self, request, id):
		rest = self.db.get_restaurant(id)
		form = RestaurantForm(obj=rest)

		if form.validate_on_submit():
			rest_query = request.form.to_dict(flat=False)
			self.db.update_restaurant(rest_query) 
			self.db.close_connection()
			
			try:
				flash('Restaurant registered correctly', 'success')
				
			except:
				self.db.rollback()
				flash('Error restaurant registeration.', 'danger')
		
		return self.page_mk.make_update_page(form)
		
	
	def delete_restaurant_controller(self, request):
		try:
			id=request.form['id']  # str
			self.db.delete_restaurant(id) 
			self.db.close_connection()
			flash('Delete successfully.', 'danger')
		except:
			self.db.rollback()
			flash('Error delete restaurant.', 'danger')
		
		return self.restaurants_list_controller()

		