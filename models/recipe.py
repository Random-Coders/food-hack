#Imports
import requests

class Recipe():
	def __init__(self):
		pass

	def get_recipe(self, food):
		r = requests.get(f'http://www.recipepuppy.com/api/?q={food}', auth=('user', 'pass'))
		return r.json()