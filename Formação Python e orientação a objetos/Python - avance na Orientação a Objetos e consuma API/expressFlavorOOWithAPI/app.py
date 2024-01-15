from restaurant.restaurant import Restaurant
from restaurant.menu.menu_dish import Dish
from restaurant.menu.menu_drink import Drink
from restaurant.menu.menu_dessert import Dessert

square_restaurant = Restaurant("Square", "Gourmet")
mexican_restaurant = Restaurant('Mexican Food', 'Mexican')
pizza_restaurant = Restaurant("speed flash", "fast food")
japanese_restaurant = Restaurant("Japa box ", "Japanese food")

square_restaurant.set_restaurant_user_review('Robert', 5, 'Bad Quality service')
square_restaurant.set_restaurant_user_review('Anne', 8, 'Good Food. \n The flavor is good!')
square_restaurant.set_restaurant_user_review('Bel', 9, 'Delicious Food. \n The flavor is magnificent!')
square_restaurant.switch_state()
# square_restaurant.mean_review_score()

juice_drink = Drink('Watermelon juice', 5.50, '500 ml')
little_bread = Dish('Little Bread', 1.99, '30[g] of potato bread')
red_cheesecake_description = ('Vanilla cake with a few tablespoons of cocoa powder and '
                              'red food coloring mixed in and layered with ermine icing.')
red_cheesecake = Dessert('Red Velvet Cheesecake', 15.65, red_cheesecake_description,
                         'sweet', '100[g] - piece')

# square_restaurant.add_drink_to_menu(juice_drink)
# square_restaurant.add_dish_to_menu(little_bread)
square_restaurant.add_item_to_menu(juice_drink)
square_restaurant.add_item_to_menu(little_bread)
square_restaurant.add_item_to_menu(red_cheesecake)
square_restaurant.show_restaurant_menu()
print()
print('--- Discount Applied ---')
juice_drink.apply_discount()
little_bread.apply_discount()
red_cheesecake.apply_discount()
square_restaurant.show_restaurant_menu()

def main():
    Restaurant.list_restaurant()

    # print(juice_drink)
    # print(little_bread)

if __name__ == '__main__':
    main()