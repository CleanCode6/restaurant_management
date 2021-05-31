# restaurant_management
CAU_Restaurant_Guide의 관리자 page로 Restaurant리스트들을 각각 CRUD합니다.
## install
pip install -r requirements.txt
python3 migrations.py
## run
python3 app.py
## project directory
1. __init__.py
* restaurants()
* register_restaurant()
* update_restaurant()
* delete_restaurant()
2. app.py
3. controller.py
* restaurants_list_controller()
* register_restaurant_controller()
* update_restaurant_controller()
* delete_restaurant_controller()
4. db_connection.py
* get_restaurants()
* get_restaurant()
* register_restaurant()
* update_restaurant()
* make_update_query
* delete_restaurant
5. db_connection_test_py
6. fields.py
7. forms.py
* restaurnat_name
* category
* score
* image
* menu
* position_x
* position_y
* address
8. model/restaurants/py
9. page_maker.py
* make_restautants_list_page()
* make_resgister_page()
* make_update_page()
10. restaurants_test.py
* * *
template 
1. forms.html
2. master.html
3. create_restaurant.html
4. restaurants.html
5. update_restaurant.html
## etc
CRUD Template: https://github.com/tanrax/flask-contacts
