from dataclasses import dataclass
import json

from pymysql import DBAPISet


@dataclass
class Restaurants(DBAPISet):
	__tablename__ = 'Restuarants'
	restaurant_id: int = 0
	distance: int = 0
	category: int = 0
	restaurant_name: str = ""
	description: str = ""
	score: float =  0.0
	pricing: str = ""
	image: str = "" # image link
	phone: str = ""
	menu: list[dict] = None
	position_x: float = 0.0
	position_y: float = 0.0
	address: str = ""


class Parser:
	@staticmethod
	def to_obj(_dict_obj):
		tmp = Restaurants(**_dict_obj)
		tmp.menu = json.loads(tmp.menu)
		return tmp

	@staticmethod
	def to_list(_dict_obj_list):
		return list(map(lambda rest: Restaurants(**rest), _dict_obj_list))