#Imports
import requests
from food import Food

class Recipe():
	def __init__(self):
		pass

	def get_recipe(self, food):
		r = requests.get(f'http://www.recipepuppy.com/api/?q={food}', auth=('user', 'pass'))
		self.json = r.json()
		return r.json()

	def parse_json(self):
		json = self.json
		results = json['results']
		foods = []
		for result in results:
			food = Food()
			food.title = result['title'] # string
			food.link = result['href'] # string 
			food.ingredients = result['ingredients'].split(", ") # list
			foods.append(food)
		self.foods = foods

# usage for the Recipe class
# if __name__ == "__main__":
# 	r = Recipe()
# 	r.get_recipe("apple")
# 	r.parse_json()
# 	print(r.foods[0].title)
# 	print(r.foods[0].link)
# 	print(r.foods[0].ingredients)