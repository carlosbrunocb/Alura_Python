import abc
from abc import ABC, abstractmethod

class MenuItem(ABC):
    def __init__(self, name, price):
        self._m_name  = name
        self._m_price = round(price, 2)

    @abc.abstractmethod
    def apply_discount(self):
        ...
