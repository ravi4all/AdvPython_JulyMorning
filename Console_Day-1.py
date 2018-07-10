Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Player():
	health = 100
	kick = False
	Punch = False

	
>>> player_1 = Player()
>>> player_1.health
100
>>> health
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    health
NameError: name 'health' is not defined
>>> type(Player)
<class 'type'>
>>> a = 10
>>> type(a)
<class 'int'>
>>> type(int)
<class 'type'>
>>> type(player_1)
<class '__main__.Player'>
>>> type(Player.health)
<class 'int'>
>>> isinstance(a, int)
True
>>> isinstance(player_1, Player)
True
>>> isinstance(a, Player)
False
>>> class Vehicle():
	tyre = 0
	engine = True
	gear = 0

	
>>> car = Vehicle()
>>> car.tyre
0
>>> car.tyre = 4
>>> car.gear = 6
>>> car
<__main__.Vehicle object at 0x00000203B0C5CD30>
>>> bike = Vehicle()
>>> bike.tyre = 2
>>> bike.gear = 5
>>> cycle = Vehicle()
>>> cycle.tyre = 2
>>> cycle.engine = False
>>> cycle.gear = 4
>>> cycle.__dict__
{'tyre': 2, 'engine': False, 'gear': 4}
>>> bike.__dict__
{'tyre': 2, 'gear': 5}
>>> car.__dict__
{'tyre': 4, 'gear': 6}
>>> bike.engine
True
>>> bike.abs
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    bike.abs
AttributeError: 'Vehicle' object has no attribute 'abs'
>>> bike.abs = True
>>> bike.__dict__
{'tyre': 2, 'gear': 5, 'abs': True}
>>> car.abs
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    car.abs
AttributeError: 'Vehicle' object has no attribute 'abs'
>>> dir(bike)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'abs', 'engine', 'gear', 'tyre']
>>> bike.__class__
<class '__main__.Vehicle'>
>>> 
