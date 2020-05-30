import typing
from abc import ABC, ABCMeta, abstractmethod
from oop.abilities import Movable, Stayable, Layable
from oop.items.books import PythonCookBook
from oop.items.drawers import TableDrawer
from oop.items.lamps import TableLamp
from phones import Iphone6
from oop.items.sheets import DefSheet


class Table(ABC):
    """
        This object represents a specific table.
        Contains 3 interfaces to implement in it's subclasses.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def stay(self) -> str:
        pass

    @abstractmethod
    def lay(self) -> str:
        pass

    @abstractmethod
    def move(self, direction: str) -> str:
        pass


class DefTable(Table):
    """ This object represents a default table. """

    def __init__(self, drawers: int = 0, *elements_on_table: typing.Any, temp,temp2):
        name = self.__class__.__name__  # composition
        self._e = elements_on_table  # aggregation
        self._d = TableDrawer(name, drawers)  # composition
        self._m = Movable(name)  # composition
        self._s = Stayable(name)  # composition
        self._l = Layable(name)  # composition

    def stay(self) -> str:
        return self._s.stay()

    def lay(self) -> str:
        return self._l.lay()

    def move(self, direction: str) -> str:
        return self._m.move(direction)

    def drawers(self) -> str:
        return self._d.amount()

    def items_on_table(self) -> str:
        if not len(self._e):
            return "{} has 0 items on it".format(self)
        return "{} has ".format(self) + ", ".join(map(lambda item: str(item), self._e)) + " on it"

    def __str__(self) -> str:
        return self.__class__.__name__


class OfficeTable(DefTable):
    """ This object represents a specific office table. """

    def summary(self) -> str:
        return "This is an office table"

    def __str__(self) -> str:
        return self.__class__.__name__


class WritingTable(DefTable):
    """ This object represents a specific writing table. """

    def summary(self) -> str:
        return "This is a writing table"

    def __str__(self) -> str:
        return self.__class__.__name__


if __name__ == '__main__':
    office = OfficeTable(4, PythonCookBook(), DefSheet(), TableLamp(), Iphone6())
    print(office.summary())
    print(office.stay())
    print(office.lay())
    print(office.move('left'))
    print(office.drawers())
    print(office.items_on_table())
