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
		# self.db.connect_to_db()

	def restaurants_list_controller(self):
		rests_query = self.db.get_restaurants()
		self.db.close_connection()
		return self.page_mk.make_restautants_list_page(rests_query)
		
	def register_restaurant_controller(self, request):
		form = RestaurantForm()
		if form.validate_on_submit():
			rest_query = request.form.to_dict(flat=False)
			del_csrf = rest_query
			del(del_csrf['csrf_token'])
			self.db.register_restaurant(del_csrf)
			
			try:
				flash('Restaurant registered correctly', 'success')
				return self.restaurants_list_controller()
			except:
				self.db.rollback()
				flash('Error restaurant registeration.', 'danger')
				return
			
		# get
		return self.page_mk.make_resgister_page(form)

	def update_restaurant_controller(self, request, restaurant_id):
		rest = self.db.get_restaurant(restaurant_id)
		form = RestaurantForm(obj=rest)

		if form.validate_on_submit():
			rest_query = request.form.to_dict(flat=False) #  rest_query = request.form
			del_csrf = rest_query
			del(del_csrf['csrf_token'])
			self.db.update_restaurant(del_csrf, restaurant_id)
			
			try:
				flash('Restaurant updated correctly', 'success')
				
			except:
				self.db.rollback()
				flash('Error restaurant update.', 'danger')
		
		return self.page_mk.make_update_page(form)
		
	
	def delete_restaurant_controller(self, request):
		try:
			restaurant_id=request.form['restaurant_id']  # str
			self.db.delete_restaurant(restaurant_id) 

			flash('Delete successfully.', 'danger')
		except:
			self.db.rollback()
			flash('Error delete restaurant.', 'danger')
		
		return self.restaurants_list_controller()

		