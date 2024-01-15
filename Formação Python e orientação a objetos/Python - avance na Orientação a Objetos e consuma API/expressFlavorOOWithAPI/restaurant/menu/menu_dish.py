from restaurant.menu.menu_item import MenuItem

class Dish(MenuItem):
    __discount = 0.08

    def __init__(self, name, price, description):
        super().__init__(name, price)
        self._m_description = description

    def __str__(self):
        '''
        String representation of Dish Menu
        :return: String Formatation
        '''
        # return (f'{self.m_name} | {self.m_category} | activated ' if self.m_active
        #        else f'{self.m_name} | {self.m_category} | deactivated ')
        return (f'{self._m_name} | {self._m_price} | {self._m_description} ')

    def apply_discount(self):
        self._m_price *= 1.0 - self.__discount
        self._m_price = round(self._m_price, 2)