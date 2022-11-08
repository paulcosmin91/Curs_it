#2 ABSTRACTIZARE
from abc import abstractmethod
class FormaGeometrica:
    PI=3.14
    @abstractmethod
    def aria(self):
        pass
    def descrie(self):
        print('Cel mai probabil am colturi.')
formageometrica1=FormaGeometrica
formageometrica1.descrie('patrat')

# INHERITANCE
class Patrat(FormaGeometrica):
    def __init__(self,latura):
        self.latura=latura
#ENCAPSULATION
    def __init__(self,latura):
        self.__latura=latura
    @property
    def latura(self):
        return self.__latura
    @latura.getter
    def get_latura(self):
        print(f'Getter:Latura are dimensiunea {self.__latura}')
        return self.__latura
    @latura.setter
    def set_latura(self,new_value):
        print(f'Setter:Noua dimensiune a laturii este: {new_value}')
        self.__latura=new_value
    @latura.deleter
    def delete_latura(self):
        print(f'Deleter:am sters dimensiunea laturii.')
        self.__latura=None
    def aria(self):
        aria=int(self.__latura)*int(self.__latura)
        return aria
class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.raza = raza
    # ENCAPSULATION
    def __init__(self, raza):
        self.__raza = raza
    @property
    def raza(self):
        return self.__raza
    @raza.getter
    def get_raza(self):
        print(f'Getter:Latura are dimensiunea {self.__raza}')
        return self.__raza
    @raza.setter
    def set_latura(self, new_value):
        print(f'Setter:Noua dimensiune a laturii este: {new_value}')
        self.__raza = new_value
    @raza.deleter
    def delete_raza(self):
        print(f'Deleter:am sters dimensiunea laturii.')
        self.__raza = None
    def aria(self):
        aria = self.PI *int(self.__raza)**2
        return aria
#polymorphism
    def descrie(self):
         print('Eu nu am colturi')
patrat1=Patrat('10')
patrat1.descrie()
patrat1.set_latura='20'
patrat1.get_latura
print(patrat1.aria())
del patrat1.delete_latura
patrat1.get_latura
cerc1=Cerc('5')
cerc1.descrie()
cerc1.set_raza='10'
cerc1.get_raza
print(cerc1.aria())
del cerc1.delete_raza
cerc1.get_raza







