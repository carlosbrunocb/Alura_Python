from ExFlavorLib.restaruant_review import Rest_Review
class Restaurant:
    '''
    Class: Restaurant class, representation of the restaurant and its characteristics
    :: Attributes: name, category, active, restaurants
    :: Methods: list_restaurant, switch_state, set_restaurant_user_review
    '''
    # m_name = ''
    # m_category = ''
    # m_active = False
    m_restaurants = [] # Kind of static attribute

    # Constructor
    def __init__(self, name, category):
        '''
        Constructor of restaurant class
        :param name: restaurant name
        :param category: type of restaurant
        '''
        self._m_name = name.title()
        self._m_category = category.upper()
        self._m_active = False
        self._restaurant_user_review_list = []
        Restaurant.m_restaurants.append(self) # Kind of static attribute

    # def __init__(this, name, category):
    #     this.m_name = name
    #     this.m_category = category
    #     self.m_active = False

    # Special method to define how to show the object's internal information
    def __str__(self):
        '''
        Restaurants string representation
        :return: String Formatation
        '''
        # return (f'{self.m_name} | {self.m_category} | activated ' if self.m_active
        #        else f'{self.m_name} | {self.m_category} | deactivated ')
        return (f'{self._m_name} | {self._m_category} | {self.m_active} ')

    # Kind of static method
    # Class method
    def list_restaurant():
        '''
        Show all restaurant added in the list
        '''
        print(f'{'# RESTAURANT NAME'.ljust(20)} # {'CATEGORY'.ljust(20)} # {'RATE'.ljust(20)} # {'STATE'}')
        for restaurant in Restaurant.m_restaurants:
            print (f'| {restaurant._m_name.ljust(19)}| {restaurant._m_category.ljust(20)} | '
                   f'{str(restaurant.mean_review_score).ljust(20)} | '
                   f'{restaurant._m_active} [{restaurant.m_active}]')
            # print (f'{restaurant.m_name} | {restaurant.m_category} | activated  ' if restaurant.m_active
            #    else f'{restaurant.m_name} | {restaurant.m_category} | deactivated  ')

    # Class Method
    @property
    def m_active(self):
        '''
        Representation of active mode
        :return: Returning a string with symbol and name activated or deactivated depends on value of _m_active
        '''
        return '✅ activated' if self._m_active else '❎ deactivated'

    def switch_state(self):
        '''
        Allow to switch the restaurant's status to activated or deactivated.
        '''
        self._m_active = not self._m_active
        print(f'>> {self._m_name} Restaurant Status Changed To ACTIVATED.' if self._m_active
              else f'>> {self._m_name} Restaurant Status Changed To DEACTIVATED.')
        print(f'{'RESTAURANT NAME'.ljust(20)} # {'CATEGORY'.ljust(20)} # {'STATE'}')
        print(f'{self._m_name.ljust(20)} | {self._m_category.ljust(20)} | {self.m_active} ')

    def set_restaurant_user_review(self, costumer, score, review_message = ''):
        '''
        Register a user assessment
        :param costumer: user name
        :param score: user score
        :param review_message: user message
        '''
        if(0 <= score <= 5):
            user_assemment = Rest_Review(costumer, score, review_message)
            self._restaurant_user_review_list.append(user_assemment)
        else:
            print(f'# Error: the input {score} is not within the range between 0 and 5.')


    @property
    def mean_review_score(self):
        '''
        Function: Compute the average if there are one or more user assessment
        :return: Return the average measure if there are reviews in the list.
        Othercase, return - [no reviews]
        '''

        if (not self._restaurant_user_review_list):
            return '-' # no assessment

        score_sum = sum(user_score._score for user_score in self._restaurant_user_review_list)
        # for user_score in self._restaurant_user_review_list:
        #     score_sum += user_score._score
        score_number = len(self._restaurant_user_review_list)

        score_mean = round(score_sum/score_number, 1)

        return score_mean
