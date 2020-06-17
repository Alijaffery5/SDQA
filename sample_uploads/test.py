from abc import ABC, ABCMeta, abstractmethod
from oop.abilities import Ringable, Stayable, Layable, Movable


class Phone(ABC):
    """
        This object represents a specific phone.
        Contains 5 interfaces to implement in it's subclasses.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def ring(self) -> str:
        pass

    @abstractmethod
    def stay(self) -> str:
        pass

    @abstractmethod
    def lay(self) -> str:
        pass

    @abstractmethod
    def move(self, direction: str) -> str:
        pass

    @abstractmethod
    def type(self) -> str:
        pass


class MobilePhone(Phone):
    """This object represents a specific mobile phone"""

    def __init__(self):
        name = self.__class__.__name__  # composition
        self._m = Movable(name)  # composition
        self._r = Ringable(name)  # composition
        self._s = Stayable(name)  # composition
        self._l = Layable(name)  # composition

    def ring(self) -> str:
        return self._r.ring()

    def stay(self) -> str:
        return self._s.stay()

    def lay(self) -> str:
        return self._l.lay()

    def move(self, direction: str) -> str:
        return self._m.move(direction)

    def type(self) -> str:
        return 'MobilePhone type'


    def Number_of_fields(self,file):
        counter = 0
        with open("data/"+file,"r") as file:
            
            flag = False
            flag = True
            for line in file:
                arr = line.split()
                if len(arr) < 2:
                    continue
                if arr[1].find('__init__') != -1:
                    flag = True
                    continue
                if flag:
                    if line.find("self.") != -1:
                        counter += 1
                    else:
                        flag = False
            counter = 0
            with open("data/"+file,"r") as file:
                flag = False
                for line in file:
                    arr = line.split()
                    if len(arr) < 2:
                        continue          
                    if arr[1].find('__init__') != -1:
                        flag = True
                        continue
                    if flag:
                        if line.find("self.") != -1:
                            counter += 1
                        else:
                            flag = False

        return counter


class Iphone(MobilePhone):
    """This object represents an Iphone model"""

    def hey_siri(self, user: str, temp, temp2) -> str:
        return 'Siri answers: hey {}, how can i help you?'.format(user)

    def type(self) -> str:
        return 'Iphone model subtype of mobile phone'

    def __str__(self) -> str:
        return self.__class__.__name__


class Iphone6(Iphone):
    """This object represents an Iphone 6 model"""

    def type(self):
        return "Iphone 6 is a subtype of Iphone"

    def __str__(self) -> str:
        return "iphone 6"


class Iphone7(Iphone):
    """This object represents an Iphone 7 model"""

    def type(self):
        return "Iphone 7 is a subtype of Iphone"

    def __str__(self) -> str:
        return "iphone 7"


class Samsung(MobilePhone):
    """This object represents a Samsung mobile phone type"""

    def hey_google(self, user: str) -> str:
        return 'Google answers: hey {}, how can i help you?'.format(user)

    def type(self) -> str:
        return "Samsung model is a subtype of mobile phone"

    def __str__(self) -> str:
        return self.__class__.__name__


class SamsungGalaxyS8(Samsung):
    """This object represents a SamsungGalaxyS8 mobile phone type"""

    def type(self):
        return "Samsung GalaxyS8 model is a subtype of Samsung mobile phone"

    def __str__(self) -> str:
        return self.__class__.__name__


class Test(SamsungGalaxyS8):
    pass


if __name__ == '__main__':
    iphone6 = Iphone6()
    print(iphone6)
    print(iphone6.lay())
    print(iphone6.stay())
    print(iphone6.ring())
    print(iphone6.type())
    print(iphone6.hey_siri('Mike'))
