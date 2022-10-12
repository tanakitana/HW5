"""W3"""
# class MyClass:
#   x = 5
#
# p1 = MyClass()      #p1 is object
# print(p1.x)         #5

"""=========="""

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
# p1 = Person("John", 36)
#
# print(p1.name, p1.age)          #John 36

"""or"""

# class Person:
#   def __init__(self, fname, age):
#     self.firstname = fname
#     self.age = age
#
#   def printname(self):
#     print(self.firstname, self.age)
#
# x = Person("John", 36)
# x.printname()

"""or"""

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def __str__(self):
#     return f"{self.name} ({self.age})"
#
# p1 = Person("John", 36)
#
# print(p1)                        #John (36)

"=========="

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def myfunc(self):
#     print("Hello my name is " + self.name)  #Hello my name is John
#
# p1 = Person("John", 36)
# p1.myfunc()

"=========="

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def myfunc(self):
#     print("Hello my name is " + self.name)
#
# p1 = Person("John", 36)
#
# print(p1.age)           #36
#
# p1.age = 40
# print(p1.age)           #40
#
# del p1.age
# print(p1.age) #AttributeError: 'Person' object has no attribute 'age'

"=========="

# class Person:
#   pass

"=========="

# class CLASS:
#   def __init__(self, actionA, actionB):
#     self.name = actionA
#     self.sing = actionB
#
# object1 = CLASS("John", "Arrrrr")
# print(object1.name)         #John
# print(object1.sing)         #Arrrrr
#
# object2 = CLASS("Jenn", "Aaaaaa")
# print(object2.name)         #Jenn
# print(object2.sing)         #Aaaaaa

"""=====================================
           INHERITANCE                  
"""
# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname
#
#   def printname(self):
#     print(self.firstname, self.lastname)
#
# class Student(Person):
#   def __init__(self, fname, lname):
#     Person.__init__(self, fname, lname)
#
# x = Student("Mike", "Olsen")
# x.printname()



"""===================================================
                CLASS                               
======================================================"""



class Employee:                    #"""PAPA"""
    def __init__(self, name, l_name):
        self.namE = name
        self.l_namE = l_name

    def work(self):
        return "I am working!"

class Developer(Employee):          #"""KID 1"""
    def __init__(self, name, l_name, language):
        super().__init__(name, l_name)
        # self.language = language
        self.__language = language

    def coding(self):
        return "I'm coding!"

    def work(self):
        return "I'm dev and I'm not working!"

    def get_language(self):
        return f"My language is {self.__language}"


class Tester(Employee):             #"""KID 2"""
    def __init__(self, name, l_name, language, test_framework):
        super().__init__(name, l_name)
        self.language = language
        self.test_framework = test_framework

    def testing(self):
        return "I can write tests!"

    def work(self):
        return "I'm on break!"


class Junior(Developer):              #"""vnyk"""
    pass

# dev1 = Developer("Max", "Frolov", "Python")
# print(dev1.work())
# print(dev1.get_language())
# print(dev1.namE)     #Max
# print(dev1.coding())     #I'm coding!
# print(dev1.language)     #Python
# print(isinstance(dev1, Developer))     #True
# print(type(dev1))           #<class '__main__.Developer'>
# print(issubclass(Developer, Employee))    #True


# tester1 = Tester("Anna", "Fedorova", "Java", "TestING")
# print(tester1.testing())   #I can write tests!
# print(tester1.work())

employee1 = Employee("Alex", "Smith")
"""
Employee - class
employee1, employee2 - class objects
"""
# print(employee1.namE)   #Alex
# print(employee1.l_namE)   #Smith
# print(employee1.work())    #I am working!
# # print(employee1.coding)    #Error, there isn't coding in Employee



# employee2 = Employee('Vlad', 'Popov')
# print(employee2.namE)
# print(employee2.l_namE)
#or KWARGS
employee2 = Employee(l_name='Popov', name="Vlad")
# print(employee2.namE)       #Vlad
# print(employee2.l_namE)     #Popov

# print(employee1.work())    #I am working!
# print(dev1.work())         #I'm not working!
# print(tester1.work())      #I'm on break!

"""======================================================
                    POLYMORPHISM                    
========================================================"""
"""Одна функция с разными результатами"""
# print(employee1.work())    #I am working!
# print(dev1.work())         #I'm not working!
# print(tester1.work())      #I'm on break!

"""======================================================
                    Абстракция
========================================================="""
"""выделяем главное, игнорируем второстепенное"""


"""======================================================
                    Инкапсуляция
========================================================="""
"""класс включает в себя методы"""
"""уровни доступа"""

# #PUBLIC:
# self.color = 'Red'
#
# #PROTECTED:
# self._color = 'Grey'
#
# #PRIVATE:
# self.__color = 'Orange' -> _Phone__color


"""class Developer(Employee):       
    def __init__(self, name, l_name, language):
        super().__init__(name, l_name)
        self.__language = language"""


# print(dev1.language)  #AttributeError: 'Developer' object
                        # has no attribute 'language'

# dev1.name = "Maxim"
# print(dev1.name)
# dev1.__language = "Java script"
# print(dev1.get_language())
# print(dev1.__language)   #AttributeError: 'Developer' object
                        # has no attribute 'language'



"""====================================================
                            GIT
======================================================="""




"""
===========================================================
            REVIEW 5.1
==========================================================="""

# from animal import Animal
#
# animal = Animal(name = 'Tuzik', weight=10, age=2)
# # print(type(animal))
# print(animal.__dict__)
# # print(animal.name)
# animal.print_info()


"""======================================================

HW
 ======================================================="""


"""5.1. Создайте любой класс с произвольным количеством подклассов,
 экземпляров, атрибутов и методов
    - как минимум один атрибут должен быть с уровнем доступа private.
     Соответственно, для получания значений этого атрибута 
    нужно использовать методы get и set
5.2. Cоздайте репозиторий на Github и отправте файл с домашним 
заданием в этот удаленный репозиторий"""

class Users:
    def __init__(self, name, specialty):
        self.namE = name
        self.specialtY = specialty

    def __str__(self):
        return f'({self.namE} - {self.specialtY})'

    def life(self):
        return "My life is game!"

    def sayHi(self):
        return "Hello I am " + self.namE

Tom = Users('Tomas200', "magic")
# print(Tom)             #(Tomas200 - magic)
# print(Tom.namE)        #Tomas200
# print(Tom.specialtY)   #magic
# print(Tom.sayHi())     #Hello I am Tomas200
# print(Tom.life())      #My life is game!

class Clan(Users):
    def __init__(self, name, specialty, clan_size):
        super().__init__(name, specialty)
        self.clan_sizE = clan_size

    def sayHi(self):
        return "Hello it's clan " + self.namE

    def clan_meet(self):
        return "We have conference every Sat at 10am"

Lions = Clan('Lions', 'magic', 315)
# print(Lions)             #(Lions - magic)
# print(Lions.namE)        #Lions
# print(Lions.specialtY)   #magic
# print(Lions.clan_sizE)   #315
# print(Lions.life())      #My life is game!
# print(Lions.sayHi())     #Hello it's clan Lions
# print(Lions.clan_meet()) #We have conference every Sat at 10am

class clan_users(Clan):
    def __init__(self, name, specialty, clan_size, clan_name, rank, password):
        super(clan_users, self).__init__(name, specialty, clan_size)
        self.clan_namE = clan_name
        self.ranK = rank
        self.agE = 18
        self.__passworD = password


    def sayHi(self):
        return f"I'm {self.namE} from clan {self.clan_namE}!"

    def print_password(self):
        return self.__passworD

John = clan_users('Zorro98', 'magic', Lions.clan_sizE, 'Lions', 'private', "QWERTY")

# print(John)             #(Zorro98 - magic)
# print(John.namE)        #Zorro98
# print(John.specialtY)   #magic
# print(John.clan_sizE)   #315
# print(John.clan_namE)   #Lions
# print(John.ranK)        #private
# John.ranK = "Warrior"
# print(John.ranK)        #Warrior
# print(John.agE)         #18
# print(John.life())      #My life is game!
# print(John.sayHi())     #I'm Zorro98 from clan Lions!
# John.l_name = 'Black'
# print(John.l_name)      #Black

# print(John.passworD)   #QWERTY
# print(John.passworD)   #'self.__passworD = password' => AttributeError
# print(John.__passworD)   #'self.__passworD = password' => AttributeError
# print(id(John.passworD))
print(John.print_password()) #QWERTY
# print(John.print_password()) #'self.__passworD = password' => AttributeError
# print(John.__print_password()) #'def __print_password' => AttributeError






