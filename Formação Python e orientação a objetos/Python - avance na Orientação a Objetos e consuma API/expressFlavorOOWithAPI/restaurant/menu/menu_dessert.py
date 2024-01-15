from restaurant.menu.menu_item import MenuItem

class Dessert(MenuItem):
    __discount = 0.15

    def __init__(self, name, price, description, type, size):
        super().__init__(name, price)
        self._m_description = description
        self._m_type        = type
        self._m_size        = size

    def __str__(self):
        '''
        String representation of Dessert Menu
        :return: String Formatation
        '''
        # return (f'{self.m_name} | {self.m_category} | activated ' if self.m_active
        #        else f'{self.m_name} | {self.m_category} | deactivated ')
        return (f'{self._m_name} | {self._m_price} | {self._m_description} | '
                f'{self._m_type} | {self._m_size}')

    def apply_discount(self):
        self._m_price *= 1.0 - self.__discount
        self._m_price = round(self._m_price, 2)