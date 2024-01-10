from ExFlavorLib.restaurant import Restaurant

square_restaurant = Restaurant("Square", "Gourmet")
mexican_restaurant = Restaurant('Mexican Food', 'Mexican')
pizza_restaurant = Restaurant("speed flash", "fast food")
japanese_restaurant = Restaurant("Japa box ", "Japanese food")

square_restaurant.set_restaurant_user_review('Robert', 5, 'Bad Quality service')
square_restaurant.set_restaurant_user_review('Anne', 8, 'Good Food. \n The flavor is good!')
square_restaurant.set_restaurant_user_review('Bel', 9, 'Delicious Food. \n The flavor is magnificent!')
square_restaurant.switch_state()
# square_restaurant.mean_review_score()

def main():
    Restaurant.list_restaurant()

if __name__ == '__main__':
    main()